        body_index_frame = kinect.get_last_body_index_frame()
        color_frame      = kinect.get_last_color_frame()
                                        
        body_index_img   = body_index_frame.reshape(((depth_height, depth_width))).astype(np.uint8) 
        color_img        = color_frame.reshape(((color_height, color_width, 4))).astype(np.uint8)
                                    
        align_color_img = utils.get_align_color_image(kinect, color_img)                               
        body_index_img= cv2.bitwise_not(body_index_img)                             
                                                            
        cv2.imshow('body index', body_index_img)                    # (424, 512)                               
        cv2.imshow('align color with body joints', align_color_img) # (424, 512)                               
        res = cv2.bitwise_and(align_color_img,align_color_img,mask = body_index_img)
        cv2.imshow('Res',res)