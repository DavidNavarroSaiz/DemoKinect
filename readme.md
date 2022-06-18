<h1>Body Recorder</h1>
<p>
Este repositorio contiene recursos necesarios para adquirir imagenes y manipular el kinectV2 
en la carpeta ejemplos kinect puede encontrar segmentos de codigo y una recopilacion de otros repositorios y scripts que se utilizaron como base para contruir el body_recorder


Body recorder se divide en dos clases , la primer clase se utiliza para adquirir los frames del kinect, extraer el esqueleto de la persona y dibujar el esqueleto. La otra Clase se encarga de adquirir frames y guardar un video final.



</p>
<h1>Como instalar</h1>
<p> crear un ambiente con python 3.6 


    pip install -r requirements.txt

    ir a la carpeta body_recorder donde encontrara instrucciones para trabajar.
</p>

<h1>Notas</h1>
<p>

<h2>Problemas en la instalacion</h2>
Si ocurren problemas en la instalacion ir al path 
    ./ejemplos kinect/Original_Pykinect2 
el cual es el repositorio original de [pykinect2](https://github.com/Kinect/PyKinect2)
ir a la carpeta *pykinect2* copiar los archivos *PykinectRuntime.py y Pykinectv2.py  * 

y pegalos en la carpeta de tu ambiente:

    C:\Users\User\.conda\envs\kinect\Lib\site-packages\pykinect2

de esa manera la libreria queeda "actualizada", la solucion se encontro en este [link](https://github.com/Kinect/PyKinect2/issues/37)



si ocurren masproblemas, se recomienda buscar  [en issues](https://github.com/Kinect/PyKinect2/issues)
</p>

<h2>Repositorios importantes</h2>
<p>
Algunos ejemplos actualizados se encuentran en:
    https://github.com/limgm/PyKinect2

esqueleto: 
    https://github.com/sshh12/LibKinect2

Capturar video:
    https://github.com/hammb/deep-human-action-recognition/blob/master/capture_dataset_kinectv2/benset_kinect_v2_capture.py
    https://github.com/CalciferZh/Kinect-Recorder/blob/master/recorder.py
    https://github.com/ostadabbas/KinectV2Recorder

body tracking and comparison
    https://github.com/fbdp1202/pyukf_kinect_body_tracking
    https://stackoverflow.com/questions/11438813/comparing-a-saved-movement-with-other-movement-with-kinect

</p>