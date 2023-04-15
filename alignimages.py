import argparse
import re
import subprocess
import astropy
from astropy.io import fits

def main():
    parser = argparse.ArgumentParser( description="Sum images, aligning to the first argument" )
    parser.add_argument( "alignto", nargs=1,
                         help="Align all images to this; will not be included in the sum" )
    parser.add_argument( "files", nargs='+',
                         help="Images to sum" )
    args = parser.parse_args()
    files = [ f for f in args.files ]

    fzmatch = re.compile( '^(.*)\.fits(\.(fz|gz))?' )
    hasfz = [ False for i in range(len(files)) ]
    filebases = []
    for i, fname in enumerate( files ):
        match = fzmatch.search( fname )
        if match is None:
            #import pdb; pdb.set_trace()
            raise RuntimeError( 'EVERYTHING IS BROKEN' )
        if match.group(3) is not None:
            hasfz[i] = True
        filebases.append( match.group(1) )
    
    hdrkws = [ '^NAXIS',
               '^RADESYS$', '^CTYPE', '^CUNIT', '^CRPIX', '^CRVAL',
               '^CD', '^PV',
               # '^FGROUPNO', '^ASTIRMS',
              ]
            
    matches = [ re.compile(m) for m in hdrkws ]

        
    with fits.open( files[0], memmap=False ) as hdus:
        header = hdus[ 1 if hasfz[0] else 0 ].header

    newheader = []
    for card in header.cards:
        keep = False
        for match in matches:
            if match.search( card.keyword ):
                keep = True
        if keep:
            newheader.append( card.image )
    newheader = "\n".join(newheader) + "\n"
        

    with open( f"{filebases[i]}.remap.head", "w" ) as ofp:
        ofp.write( newheader )
    command = ["swarp"]
    command.extend( files )
    command.extend( [ "-SUBTRACT_BACK", "Y", "-DELETE_TMPFILES", "Y",
               "-IMAGEOUT_NAME", "ifitsELAIS_E1_42.coadd.fits", 
               "-WEIGHTOUT_NAME", "ifitsELAIS_E1_42.coadd.weight.fits", "-COMBINE_TYPE", "CLIPPED",
               "-CENTER_TYPE", "MANUAL", "-CENTER", " 8.08646657166521,-43.25817152099695", "-IMAGE_SIZE", "4096,2048",
               "-RESAMPLE_DIR", "./" ] )
    # import pdb; pdb.set_trace()
    subprocess.run( command )

        #!/bin/bash
#!/bin/bash


# ======================================================================

if __name__ == "__main__":
    main()
