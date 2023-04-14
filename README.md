# DECATimaging-
Code for aligning DECAT images 
1. **Edit alignimages-Copy1.py** and include the center RA and DEC that was found  for the image you want to align all other images too. Also, edit with what you want to name the final stacked fits file
2. **Run bash shifter.sh** to go into curveball image
3. **Run alignimages-Copy1.py** image1pathway allotherimagespathway 
(image 1: image you will be aligning them all too) (all other images: pathway to all images including * at the end to account for them all) 
alignimages-Copy1.py /global/u2/a/autumnaw/WorkinginDecatDatabase/DECATfields/ELAIS_E2/ELAIS_E2_g/cc4d_……chipnum_filter.fits   
/global/u2/a/autumnaw/WorkinginDecatDatabase/DECATfields/ELAIS_E2/ELAIS_E2_g/c* 
4. Need to run this 3 times per survey to account for all filters for each field
5. **Run stiff** on the three finalized, stacked, and aligned images in each filter (this only works for three filters though, no more than that)
