# DECATimaging-
Code for aligning DECAT images 
1. **Use 1cutoffsforsurveys.ipynb** to pull all the images from the database, and apply cutoffs to seeing, magzp, and skysig to pull out the quality images
2. **Use 2downloadfitsfiles.ipynb** to take the dataframes with the quality images, and download the fits files off the database to then use for stacking
3. Once all fits files are downloaded (this may take up a lot of memory), **pick a good image to run through 3findcenter.ipynb**, which will give the center RA and center DEC to align all the other images when stacking with swarp
**Edit alignimages.py** and include the center RA and DEC as parameters for the "-CENTER" argument that was found for the good image you want to align all other images too. Also, edit the file with what you want to name the final stacked and aligned image file under "-IMAGEOUT_NAME" and "-WEIGHTOUT_NAME"

4. **Run bash shifter.sh** to go into curveball image. In order to set this up, and to access curveball more info at: https://gitlab.com/robknop/curveball
5. **Run alignimages.py** image1pathway allotherimagespathway 
      
      This uses swarp to stack the images
      (image 1: image you will be aligning them all too) (all other images: pathway to all images including * at the end to account for them all) 
      python alignimages.py /global/u2/a/autumnaw/WorkinginDecatDatabase/DECATfields/ELAIS_E2/ELAIS_E2_g/cc4d_……chipnum_filter.fits   
      /global/u2/a/autumnaw/WorkinginDecatDatabase/DECATfields/ELAIS_E2/ELAIS_E2_g/c* 

6. Need to run alignimages.py three times per survey to account for all filters within each field. 

7. **Run stiff** on the three finalized, stacked, and aligned images (so the g, r, and i filter images) for each survey. Stiff can be downloaded from the .tar file. This will give one final .tif image for one chipnumber for the survey (this only works for three filters though, no more than that). **To convert this tif to a jpg, use converttiftojpg.ipynb**

8. Makingrgbimages.ipynb can be used for plotting individual fits files and stacking them on top of each other, but stacking them will only work if they are already properly aligned.
