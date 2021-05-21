import cv2
import numpy as np

from . inference import yolov5_prediction,img_preprocessing
from . post_processing import detect_post_processing,track_post_processing,dense_post_processing,count_post_processing,field_post_processing


def Detection_Processing(input_img,save_path,yolo5_config,model,class_names,cameArea,class_colors=None):
    try:
        tensor_img=img_preprocessing(input_img,yolo5_config.device,yolo5_config.img_size)
        pred=yolov5_prediction(model,tensor_img,yolo5_config.conf_thres, yolo5_config.iou_thres,yolo5_config.classes)
        result_img=detect_post_processing(input_img,pred,class_names,tensor_img.shape,cameArea,class_colors)
        cv2.imwrite(save_path,result_img)
        return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    
def Tracking_Processing(input_img,save_path,yolo5_config,model,class_names,cameArea,Tracker,class_colors=None):
    try:
        tensor_img=img_preprocessing(input_img,yolo5_config.device,yolo5_config.img_size)
        pred=yolov5_prediction(model,tensor_img,yolo5_config.conf_thres, yolo5_config.iou_thres,yolo5_config.classes)
        result_img=track_post_processing(input_img,pred,class_names,tensor_img.shape,cameArea,Tracker,class_colors)
        cv2.imwrite(save_path,result_img)
        return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    
def Denseing_Processing(input_img,save_path,yolo5_config,model,class_names,cameArea,class_colors=None):
    try:
        tensor_img=img_preprocessing(input_img,yolo5_config.device,yolo5_config.img_size)
        pred=yolov5_prediction(model,tensor_img,yolo5_config.conf_thres, yolo5_config.iou_thres,yolo5_config.classes)
        result_img=dense_post_processing(input_img,pred,class_names,tensor_img.shape,cameArea,class_colors)
        cv2.imwrite(save_path,result_img)
        return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    
def Counting_Processing(input_img,save_path,yolo5_config,model,class_names,theLine,Tracker,Obj_Counter,class_colors=None):
    try:
        tensor_img=img_preprocessing(input_img,yolo5_config.device,yolo5_config.img_size)
        pred=yolov5_prediction(model,tensor_img,yolo5_config.conf_thres, yolo5_config.iou_thres,yolo5_config.classes)
        result_img=count_post_processing(input_img,pred,class_names,tensor_img.shape,theLine,Tracker,Obj_Counter,class_colors)
        cv2.imwrite(save_path,result_img)
        return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    
def Vector_Field_Processing(input_img,save_path,yolo5_config,model,class_names,Field,Tracker,class_colors=None):
    try:
        tensor_img=img_preprocessing(input_img,yolo5_config.device,yolo5_config.img_size)
        pred=yolov5_prediction(model,tensor_img,yolo5_config.conf_thres, yolo5_config.iou_thres,yolo5_config.classes)
        result_img=field_post_processing(input_img,pred,class_names,tensor_img.shape,Field,Tracker,class_colors)
        cv2.imwrite(save_path,result_img)
        return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    
def Trace_Mask_Processing(input_img,save_path,yolo5_config,model,class_names,cameArea,Tracker,class_colors=None):
    try:
        tensor_img=img_preprocessing(input_img,yolo5_config.device,yolo5_config.img_size)
        pred=yolov5_prediction(model,tensor_img,yolo5_config.conf_thres, yolo5_config.iou_thres,yolo5_config.classes)
        result_img=track_post_processing(input_img,pred,class_names,tensor_img.shape,cameArea,Tracker,class_colors)
        cv2.imwrite(save_path,result_img)
        return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    
def Background_Modeling(input_img,save_path,bg_model,target='vis'):
    try:
        fg_mask = bg_model.apply(input_img)
        bg_img = bg_model.getBackgroundImage()
        if target=='fg_mask':
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
            cv2.imwrite(save_path,fg_mask)
            return True,save_path
        elif target=='bg_img':
            cv2.imwrite(save_path,bg_img)
            return True,save_path
        elif target=='vis':
            cv2.putText(input_img,"origin image",(5,80),cv2.FONT_HERSHEY_TRIPLEX, 1.6, [0,200,0],thickness=3)
            cv2.putText(bg_img,"background image",(5,80),cv2.FONT_HERSHEY_TRIPLEX, 1.6, [0,200,0],thickness=3)
            result=np.vstack([input_img, bg_img])
            cv2.imwrite(save_path,result)
            return True,save_path
    except Exception as e:
        print("Wrong:",e,save_path)
        return False,e
    