# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:19:07 2020

Proyecto final, procesamiento de imágenes

@author: Andrea Ruiz, Sebastian Parrado & Pablo Mosquera
"""

#Librerias necesarias
import numpy as np
import cv2
import pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()


class Project:
    
    def __init__(self, img):
        
        self.img_original = img
        self.img_copy = self.img_original.copy()
        self.BGD_model = np.zeros((1,65),np.float64)
        self.FGD_model = np.zeros((1,65),np.float64)
        self.ini_points , self.fin_points , self.temp_points  , self.corners = [],[],[],[]
        self.flag_rect = True #Rect = True
        self.flag_circle_fg = False
        self.flag_circle_bg = False
        self.start = False
        self.flag_rect_or_mask = True #Rect_iteration = True / mask_iteration = False
        self.initial_mask = np.zeros(self.img_copy.shape[:2],np.uint8)
        self.mask = np.zeros(self.img_original.shape[:2],np.uint8)
        
    def click_event(self,event, x, y, flags, params):
        cv2.imshow('image',self.img_copy)
        
        if event == cv2.EVENT_LBUTTONDOWN:
            
            if self.flag_rect == True:        
                self.ini_points = [x , y]
                
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_rect == True:
                img_temp_m = self.img_original.copy()
                self.fin_points = [x , y]
                self.img_copy = cv2.rectangle(img_temp_m, tuple(self.ini_points), tuple(self.fin_points), (0, 0, 255), 5)    
                
        elif event == cv2.EVENT_LBUTTONUP:
            if self.flag_rect == True:
                img_temp = self.img_original.copy()
                self.fin_points = [x , y]
                self.img_copy = cv2.rectangle(img_temp, tuple(self.ini_points), tuple(self.fin_points), (0, 0, 255), 5)
                self.mask = cv2.rectangle(self.mask, tuple(self.ini_points), tuple(self.fin_points), 3, -1)
                self.corners = self.ini_points[0],self.ini_points[1],self.fin_points[0],self.fin_points[1]
                #self.flag_rect = False
                print('Rectangulo terminado')
                #cv2.destroyWindow('image_mod')
                self.flag_rect = False
                #self.iteration_rect()
                #self.flag_circle = True    
            #elif self.flag_circle_fg == True or self.flag_circle_bg == True: 
                #self.flag_circle_fg = False   
            #self.start == False
                #cv2.waitKey(10)
                
        if event == cv2.EVENT_LBUTTONDOWN:
            if ((self.flag_rect == False) and ((self.flag_circle_fg == True) or (self.flag_circle_bg == True))):
                self.start = True
                print("Circulo start")
                
        elif event == cv2.EVENT_LBUTTONUP: 
            print("Circulo terminado")
            self.start = False
            
                #cv2.waitKey(10)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_circle_fg == True and self.start == True: 
                print("Circulo fg")
                cv2.circle(self.img_copy, (x, y), 5, (255,255,255), -1)
                cv2.circle(self.mask, (x, y), 5, 1, -1)    
            elif self.flag_circle_bg == True and self.start == True: 
                print("Circulo bg")
                cv2.circle(self.img_copy, (x, y), 5, (0,0,0), -1)
                cv2.circle(self.mask, (x, y), 5, 0, -1)
                
    # def iteration_rect(self):
    #     #if self.flag_rect == True:
    #     cv2.grabCut(self.img_original, self.initial_mask, tuple(self.corners), self.BGD_model, self.FGD_model, 1, cv2.GC_INIT_WITH_RECT)
    #     self.mask = np.where((self.initial_mask==1)|(self.initial_mask==3), 1, 0).astype('uint8')
    #     output = cv2.bitwise_and(self.img_original, self.img_original, mask=self.mask)
    #     cv2.imshow('image_mod',output)
    #         #self.flag_rect_or_mask == False
    #         #return output 
    #     # if self.flag_rect_or_mask == False:
                
    def iteration(self):
        cv2.grabCut(self.img_original, self.mask, None, self.BGD_model, self.FGD_model, 1, cv2.GC_INIT_WITH_MASK)
        self.mask_out = np.where((self.mask==1)|(self.mask==3), 1, 0).astype('uint8')
        output = cv2.bitwise_and(self.img_original, self.img_original, mask=self.mask_out)
        cv2.imshow('image_mod',output)
            
            
    def Run(self):
            cv2.imshow('image', self.img_original)
            print("Comenzo")
            while True:
                cv2.setMouseCallback('image',  self.click_event)
                k = cv2.waitKey(1)
                #print('llegue aqui 2')
                #print(self.corners)
                if k == ord('i'):
                    print("Iteracion")
                    self.iteration()
            
                if k == ord('f'):
                    print("primer plano")
                    self.flag_circle_fg = True
                    self.flag_circle_bg = False
            
                if k == ord('b'):
                    print("fondo")
                    self.flag_circle_bg = True
                    self.flag_circle_fg = False
            
                if k == ord('q'):
                    print("Se acabo")
                    break
            
            cv2.destroyAllWindows()
                    
img = cv2.imread('lena.jpg', 1)          
            
if __name__ == '__main__':
    print(__doc__)
    Project(img = img).Run()
    cv2.destroyAllWindows()            
                    
        
    
        
    