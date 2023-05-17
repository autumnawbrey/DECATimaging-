shifter --volume="/global/homes/a/autumnaw/curveball:/curveball;/global/homes/a/autumnaw/secrets:/secrets;/pscratch/sd/a/autumnaw:/data" --image=rknop/curveball -e TERM=xterm -e CURVEBALL_CONFIG=curveball_ztf /bin/bash

#volumes - file systems in container pointing to ones outside of it 
