from cv2 import *
import numpy as np


def mouse_fonksiyonu ( *param):
    global character_image

    if ( param [ 3 ] == 1 ):
        #x , y terslendi...
        character_image [ param [ 2 ] - 3 : param[ 2 ] +3 , param [ 1 ] -3 : param[ 1 ] + 3] = 255
        imshow ( "Bos" , character_image )


   # print "Parameters : " , param


resized = None

character_image = np.zeros ( (300 , 300 , 1 ) , np.uint8 )
namedWindow( "Bos" , WINDOW_AUTOSIZE )
namedWindow("Resized" , WINDOW_AUTOSIZE )
imshow ( "Bos" , character_image )

setMouseCallback( "Bos" , mouse_fonksiyonu , None )

karakter_ismi = "sifir"


start_number = 0

follow_image = np.zeros ( ( 300 , 300 , 3 ) , np.uint8 )


number = start_number

tus = ""
while tus != 27:
    tus = waitKey( 0 )
    #cizilecek resmi resetliyoruz...
    if ( tus == ord ('r')):
        character_image [ : ] = 0
        imshow ( "Bos" , character_image )
    #karakter ismini giriyoruz...
    if tus == ord ( 'c' ):
        karakter_ismi = raw_input( "Karakter ismi : " )
        number = start_number

    if tus == ord ( 'k' ):
        clone = character_image.copy ( )
        contours , hier = findContours( character_image , RETR_EXTERNAL , CHAIN_APPROX_SIMPLE )
        character_image = clone
        follow_image [ : ] = character_image [ : ]

        for index in range ( 0 , len(contours ) ):
            x, y, w, h = boundingRect(contours[index])
            rectangle ( follow_image , ( x , y ) , ( x + w , y + h ) , ( 0,255 ,0 ) )
        imshow ( "Follow" , follow_image )
        print "Hier : " , hier

        #print "Contours" , contours
        #print "Hier : " , hier
        #print "Lem hier : " , len ( contours ),
        x,y,w,h = boundingRect( contours [ 0 ] )

        char_res = character_image [ y:y+h , x:x+w ]




        resized = resize  ( char_res , ( 28 , 28 ) )
        imshow ( "Resized" , resized)


    #kucuk resmi kaydediyoruz...
    if tus == ord ( 's' ):

        dosya_adi = karakter_ismi + str ( number ) ;
        number += 1
        if resized is not None:

            imwrite ( dosya_adi + ".jpg" , resized )
            print "Resim ismi : " + dosya_adi + ".jpg"
            print "Resim kaydedildi.."

        else:
            print "Hata : Resim kaydedilmedi..."
            number -= 1







