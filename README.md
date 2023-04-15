# DECATimaging-
Code for aligning DECAT images 
1. **Use 1cutoffsforsurveys.ipynb** to pull all the images from the database, and apply cutoffs to seeing, magzp, and skysig to pull out the quality images
2. **Use 2downloadfitsfiles.ipynb** to take the dataframes with the quality images, and download the fits files off the database to use then use for stacking
3. Once all fits files are downloaded (this may take up a lot of memory), **pick a good image to run through 3findcenter.ipynb**, which will give the center RA and center DEC to align all the other images when stacking with swarp
**Edit alignimages.py** and include the center RA and DEC that was found  for the image you want to align all other images too. Also, edit with what you want to name the final stacked fits file
4. **Run bash shifter.sh** to go into curveball image
5. **Run alignimages.py** image1pathway allotherimagespathway 
      This uses swarp to stack the images
      (image 1: image you will be aligning them all too) (all other images: pathway to all images including * at the end to account for them all) 
      alignimages-Copy1.py /global/u2/a/autumnaw/WorkinginDecatDatabase/DECATfields/ELAIS_E2/ELAIS_E2_g/cc4d_……chipnum_filter.fits   
      /global/u2/a/autumnaw/WorkinginDecatDatabase/DECATfields/ELAIS_E2/ELAIS_E2_g/c* 

6. Need to run this 3 times per survey to account for all filters for each field

7. **Run stiff** on the three finalized, stacked, and aligned images in each filter (this only works for three filters though, no more than that)
