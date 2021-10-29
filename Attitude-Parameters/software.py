#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 21 09:20:05 2021

@author: geovani ribeiro & william reis & katia candioto gandolpho
"""

from tkinter import * 
import numpy as np
import webbrowser

menu_inicial = Tk()
menu_inicial.title('Graphical User Interface for Attitude Coordinates of Satellites')
#menu_inicial.iconbitmap('@/home/geovani/Documentos//Attitude-Parameters/icon.xbm')    
#menu_inicial.call('wm', 'iconphoto', menu_inicial._w, PhotoImage(file='/home/geovani/Documentos/Attitude-Parameters/icon.gif'))
#menu_inicial['bg'] = "black"

menu_inicial.resizable(0, 0)

 
#menu_inicial.minsize(860, 200)
#menu_inicial.maxsize(960, 200)

#altura e largura do programa
largura = 860
altura = 200

#resolução
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

#posicao da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#definir a geometria
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

#definir como iconic
menu_inicial.state('iconic')
           
def helpc():
    toph = Toplevel()
    toph.title = ('Help')
    toph.resizable(0, 0)
    largura = 470
    altura = 100
    
    #resolução
    largura_screen = toph.winfo_screenwidth()
    altura_screen = toph.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    toph.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    #definir como iconic
    toph.state('iconic')
    
    labelh = Label(toph,
                    text = "This is Graphical User Interface produced by Geovani Augusto Xavier Ribeiro \n Oriented by Dr. William Reis Silva and Dr. Katia Cristiane Gandolpho Candioto",
                    font = "Arial 8",
                    anchor = N,
                    justify = RIGHT
                    ).grid(row= 1, column = 1)

    label = Label(toph,
                text = "For more information: ",   
                font = "Arial 8"      
                ).grid(row=2, column=1)   

    link1 = Label(toph, text="https://github.com/geovani-ribeiro/attitude-parameters", fg="blue", cursor="hand2")
    link1.grid(row=3, column=1)
    link1.bind("<Button-1>", lambda: webbrowser.open("https://github.com/geovani-ribeiro/attitude-parameters"))

    

#funções para o algoritmo   
def command1():    
    top1 = Toplevel()
    top1.title= ('Graphical User Interface for Attitude Coordinates of Satellites')
    top1.resizable(0, 0)
   # top1.iconbitmap('@/home/geovani/Documentos/icon.xbm')    
    #altura e largura do programa
    largura = 980
    altura = 200
    
    #resolução
    largura_screen = top1.winfo_screenwidth()
    altura_screen = top1.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    top1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    top1.maxsize(1000, 200)
    #definir como iconic
    top1.state('iconic')
    
    #definição das mensagens
    label_5 = Label(top1,
                    text = "Enter the DCM data:",
                    font = "Arial 11",
                    justify = LEFT
                    ).grid(row= 1, column = 1)
    
    #final
    phi_final = StringVar()
    e_final = StringVar()
    beta_final = StringVar()
    q_final = StringVar()
    sigma_final = StringVar()
    euler_final = StringVar()
    
    #funcao
    def dcm_calc():
        cos_Phi = 1/2*(float(C11.get())+float(C22.get())+float(C33.get())-1)
        Phi = np.arccos(cos_Phi)
        e11 = 1/(2*np.sin(Phi))*(float(C23.get())-float(C32.get()))
        e12 = 1/(2*np.sin(Phi))*(float(C31.get())-float(C13.get()))
        e13 = 1/(2*np.sin(Phi))*(float(C12.get())-float(C21.get()))
        e = np.array([e11,e12,e13])
        beta02 = 1/4*(1+float(C11.get())+float(C22.get())+float(C33.get()))
        beta12 = 1/4*(1+2*float(C11.get())-1*(float(C11.get())+float(C22.get())+float(C33.get())))
        beta22 = 1/4*(1+2*float(C22.get())-1*(float(C11.get())+float(C22.get())+float(C33.get())))
        beta32 = 1/4*(1+2*float(C33.get())-1*(float(C11.get())+float(C22.get())+float(C33.get())))
        EP = np.array([beta02, beta12, beta22, beta32])
        EP.max()
        if beta02 == EP.max():
            beta0 = np.sqrt(beta02)
            beta1 = (float(C23.get())-float(C32.get()))/(4*beta0)
            beta2 = (float(C31.get())-float(C13.get()))/(4*beta0)
            beta3 = (float(C12.get())-float(C21.get()))/(4*beta0)
        elif beta12 == EP.max():
            beta1 = np.sqrt(beta12)
            beta0 = (float(C23.get())-float(C32.get()))/(4*beta1)
            beta2 = (float(C12.get())-float(C21.get()))/(4*beta1)
            beta3 = (float(C31.get())+float(C13.get()))/(4*beta1)
        elif beta22 == EP.max():
            beta2 = np.sqrt(beta22)
            beta0 = (float(C31.get())-float(C13.get()))/(4*beta2)
            beta1 = (float(C12.get())+float(C21.get()))/(4*beta2)
            beta3 = (float(C23.get())+float(C32.get()))/(4*beta2)
        else:
            beta3 = np.sqrt(beta32)
            beta0 = (float(C12.get())-float(C21.get()))/(4*beta3)
            beta1 = (float(C31.get())+float(C13.get()))/(4*beta3)
            beta2 = (float(C23.get())+float(C32.get()))/(4*beta3)
        beta = np.array([beta0, beta1, beta2, beta3])
        q = np.tan(Phi/2)*e
        sigma = np.tan(Phi/4)*e
        psi = np.rad2deg(np.arctan(float(C12.get())/float(C11.get())))
        theta = np.rad2deg(-1*np.arcsin(float(C13.get())))
        phi = np.rad2deg(np.arctan(float(C23.get())/float(C33.get())))

        #sets
        euler_final.set("The Euler Angles is (" + str(round(psi,3)) + ", " +str(round(theta,3)) +", " +str(round(phi,3))+ ")")
        phi_final.set(r'The angle principal rotation vector is ' + str(round(np.rad2deg(Phi),3)) + '°')
        e_final.set(r'The principal rotation vector is ' + str(e)) 
        beta_final.set("The quaternion is "+str(beta))
        q_final.set("The classical Rodrigues parameters is "+ str(q))
        sigma_final.set("The modified Rodrigues parameters is " + str(sigma))
            
    #widgets
    label_C11 = Label(top1, text='C11:')
    label_C21 = Label(top1, text='C21:')
    label_C31 = Label(top1, text='C31:')
    label_C12 = Label(top1, text='C12:')
    label_C22 = Label(top1, text='C22:')
    label_C32 = Label(top1, text='C23:')
    label_C13 = Label(top1, text='C31:')
    label_C23 = Label(top1, text='C32:')
    label_C33 = Label(top1, text='C33:')
    C11 = Entry(top1)
    C21 = Entry(top1)
    C31 = Entry(top1)
    C12 = Entry(top1)
    C22 = Entry(top1)
    C32 = Entry(top1)
    C13 = Entry(top1)
    C23 = Entry(top1)
    C33 = Entry(top1)
    
    #layout
    label_C11.grid(row=2, column=1)
    C11.grid(row=2, column = 2)
    label_C12.grid(row=2, column=3)
    C12.grid(row=2, column = 4)
    label_C13.grid(row=2, column=5)
    C13.grid(row=2, column = 6)
    label_C21.grid(row=3, column=1)
    C21.grid(row=3, column = 2)
    label_C22.grid(row=3, column=3)
    C22.grid(row=3, column = 4)
    label_C23.grid(row=3, column=5)
    C23.grid(row=3, column = 6)
    label_C31.grid(row=4, column=1)
    C31.grid(row=4, column = 2)
    label_C32.grid(row=4, column=3)
    C32.grid(row=4, column = 4)
    label_C33.grid(row=4, column=5)
    C33.grid(row=4, column = 6)
    
    
    #foco
    C11.focus()
    
    
    btn1 = Button(top1,
                 text = "Calculate",
                 command = dcm_calc
                 ).grid(row = 5, column = 6)
    
    label_euler = Label(top1,textvar=euler_final).grid(rowspan=6,column=1,stick=W)
    label_phi = Label(top1,textvariable=phi_final).grid(rowspan=6, column = 1, stick= W)
    label_e = Label(top1,textvariable=e_final).grid(rowspan=6, column = 1, stick=W)
    label_beta = Label(top1,textvariable=beta_final).grid(rowspan=6, column = 1, stick=W)
    label_q = Label(top1,textvariable=q_final).grid(rowspan=6, column = 1, stick=W)
    label_sigma = Label(top1,textvariable=sigma_final).grid(rowspan=6, column = 1, stick=W)
       
def command2():    
    top2 = Toplevel()
    top2.title= ('Graphical User Interface for Attitude Coordinates of Satellites')
    top2.resizable(False, False)
    #top2.iconbitmap('@/home/geovani/Documentos/icon.xbm')    
    #altura e largura do programa
    largura = 860
    altura = 200
    
    #resolução
    largura_screen = top2.winfo_screenwidth()
    altura_screen = top2.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    top2.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    #definir como iconic
    top2.state('iconic')
    
    #definição das mensagens
    label_5 = Label(top2,
                    text = "Enter the Angle Euler (3-2-1) in deg:",
                    font = "Arial 11",
                    justify = LEFT
                    ).grid(row= 1, column = 1)
    
    #final
    phi_final = StringVar()
    e_final = StringVar()
    beta_final = StringVar()
    q_final = StringVar()
    sigma_final = StringVar()
    
    
    #funcao
    def euler_calc():
        C11 = np.cos(np.deg2rad(float(thetaEu.get())))*np.cos(np.deg2rad(float(PsiEu.get())))
        C12 = np.cos(np.deg2rad(float(thetaEu.get())))*np.sin(np.deg2rad(float(PsiEu.get())))
        C13 = -np.sin(np.deg2rad(float(thetaEu.get())))
        C21 = np.sin(np.deg2rad(float(phiEu.get())))*np.sin(np.deg2rad(float(thetaEu.get())))*np.cos(np.deg2rad(float(PsiEu.get())))-np.cos(np.deg2rad(float(phiEu.get())))*np.sin(np.deg2rad(float(PsiEu.get())))
        C22 = np.sin(np.deg2rad(float(phiEu.get())))*np.sin(np.deg2rad(float(thetaEu.get())))*np.sin(np.deg2rad(float(PsiEu.get())))+np.cos(np.deg2rad(float(phiEu.get())))*np.cos(np.deg2rad(float(PsiEu.get())))
        C23 = np.sin(np.deg2rad(float(phiEu.get())))*np.cos(np.deg2rad(float(thetaEu.get())))
        C31 = np.cos(np.deg2rad(float(phiEu.get())))*np.sin(np.deg2rad(float(thetaEu.get())))*np.cos(np.deg2rad(float(PsiEu.get())))+np.sin(np.deg2rad(float(phiEu.get())))*np.sin(np.deg2rad(float(PsiEu.get())))
        C32 = np.cos(np.deg2rad(float(phiEu.get())))*np.sin(np.deg2rad(float(thetaEu.get())))*np.sin(np.deg2rad(float(PsiEu.get())))-np.sin(np.deg2rad(float(phiEu.get())))*np.cos(np.deg2rad(float(PsiEu.get())))
        C33 = np.cos(np.deg2rad(float(phiEu.get())))*np.cos(np.deg2rad(float(thetaEu.get())))
        
        cos_Phi = 1/2*(C11+C22+C33-1)
        Phi = np.arccos(cos_Phi)
        Phideg = np.rad2deg(Phi)
        e11 = 1/(2*np.sin(Phi))*(C23-C32)
        e12 = 1/(2*np.sin(Phi))*(C31-C13)
        e13 = 1/(2*np.sin(Phi))*(C12-C21)
        e = np.array([e11,e12,e13])
        beta02 = 1/4*(1+C11+C22+C33)
        beta12 = 1/4*(1+2*C11-1*(C11+C22+C33))
        beta22 = 1/4*(1+2*C22-1*(C11+C22+C33))
        beta32 = 1/4*(1+2*C33-1*(C11+C22+C33))
        EP = np.array([beta02, beta12, beta22, beta32])
        EP.max()
        if beta02 == EP.max():
            beta0 = np.sqrt(beta02)
            beta1 = (C23-C32)/(4*beta0)
            beta2 = (C31-C13)/(4*beta0)
            beta3 = (C12-C21)/(4*beta0)
        elif beta12 == EP.max():
            beta1 = np.sqrt(beta12)
            beta0 = (C23-C32)/(4*beta1)
            beta2 = (C12-C21)/(4*beta1)
            beta3 = (C31+C13)/(4*beta1)
        elif beta22 == EP.max():
            beta2 = np.sqrt(beta22)
            beta0 = (C31-C13)/(4*beta2)
            beta1 = (C12+C21)/(4*beta2)
            beta3 = (C23+C32)/(4*beta2)
        else:
            beta3 = np.sqrt(beta32)
            beta0 = (C12-C21)/(4*beta3)
            beta1 = (C31+C13)/(4*beta3)
            beta2 = (C23+C32)/(4*beta3)
        beta = np.array([beta0, beta1, beta2, beta3])
        q = np.tan(Phi/2)*e
        sigma = np.tan(Phi/4)*e
    
        #sets
        phi_final.set(r'The angle principal rotation vector is ' + str(round(Phideg,3)) + '°')
        e_final.set(r'The principal rotation vector is ' + str(e))
        beta_final.set("The quaternion is "+str(beta))
        q_final.set("The classical Rodrigues parameters is "+ str(q))
        sigma_final.set("The modified Rodrigues parameters is " + str(sigma))
        

    #widgets
    label_PsiEu = Label(top2, font = "Arial 10", text= 'ψ')
    label_thetaEu = Label(top2, font = "Arial 10", text= 'θ')
    label_phiEu = Label(top2, font = "Arial 10", text= 'ϕ')
    PsiEu = Entry(top2)
    thetaEu = Entry(top2)
    phiEu = Entry(top2)
    
    
    #layout
    label_PsiEu.grid(row=2, column=1)
    PsiEu.grid(row=2, column = 2)
    label_thetaEu.grid(row=3, column=1)
    thetaEu.grid(row=3, column = 2)
    label_phiEu.grid(row=4, column=1)
    phiEu.grid(row=4, column = 2)
    
    #focus
    PsiEu.focus()
    
    #botao
    btn1 = Button(top2,
                 text = "Calculate",
                 command = euler_calc
                 ).grid(row = 5, column = 2)
    
    #plots
    label_phi = Label(top2,textvariable=phi_final).grid(rowspan=6, column = 1, stick= W)
    label_e = Label(top2,textvariable=e_final).grid(rowspan=6, column = 1, stick=W)
    label_beta = Label(top2,textvariable=beta_final).grid(rowspan=6, column = 1, stick=W)
    label_q = Label(top2,textvariable=q_final).grid(rowspan=6, column = 1, stick=W)
    label_sigma = Label(top2,textvariable=sigma_final).grid(rowspan=6, column = 1, stick=W)
    
def command3():    
    top3 = Toplevel()
    top3.title = ('Graphical User Interface for Attitude Coordinates of Satellites')
    top3.resizable(False, False)
    #top3.iconbitmap('@/home/geovani/Documentos/icon.xbm')   
    #altura e largura do programa
    largura = 860
    altura = 200
    
    #resolução
    largura_screen = top3.winfo_screenwidth()
    altura_screen = top3.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    top3.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    #definir como iconic
    top3.state('iconic')

    
    #definição das mensagens
    label_3 = Label(top3,
                    text = "Enter the principal rotation vector such that angle is in deg",
                    font = "Arial 11",
                    justify = LEFT
                    ).grid(row= 1, column = 1)
    
    #final
    beta_final = StringVar()
    q_final = StringVar()
    sigma_final = StringVar()
    euler_final = StringVar()
    
    #function
    def prv_calc():
        Σ = 1-np.cos(np.deg2rad(float(Phi.get())))
        C11 = float(e11.get())**2*Σ+np.cos(np.deg2rad(float(Phi.get())))
        C12 = float(e11.get())*float(e12.get())*Σ + float(e13.get())*np.sin(np.deg2rad(float(Phi.get())))
        C13 = float(e11.get())*float(e13.get())*Σ - float(e12.get())*np.sin(np.deg2rad(float(Phi.get())))
        C21 = float(e12.get())*float(e11.get())*Σ - float(e13.get())*np.sin(np.deg2rad(float(Phi.get())))
        C22 = float(e12.get())**2*Σ+np.cos(np.deg2rad(float(Phi.get())))
        C23 = float(e12.get())*float(e13.get())*Σ + float(e11.get())*np.sin(np.deg2rad(float(Phi.get())))
        C31 = float(e13.get())*float(e11.get())*Σ + float(e12.get())*np.sin(np.deg2rad(float(Phi.get())))
        C32 = float(e13.get())*float(e12.get())*Σ - float(e11.get())*np.sin(np.deg2rad(float(Phi.get())))
        C33 = float(e13.get())**2*Σ+np.cos(np.deg2rad(float(Phi.get())))  
        e = np.array([float(e11.get()),float(e12.get()),float(e13.get())])
        beta02 = 1/4*(1+C11+C22+C33)
        beta12 = 1/4*(1+2*C11-1*(C11+C22+C33))
        beta22 = 1/4*(1+2*C22-1*(C11+C22+C33))
        beta32 = 1/4*(1+2*C33-1*(C11+C22+C33))
        EP = np.array([beta02, beta12, beta22, beta32])
        EP.max()
        if beta02 == EP.max():
            beta0 = np.sqrt(beta02)
            beta1 = (C23-C32)/(4*beta0)
            beta2 = (C31-C13)/(4*beta0)
            beta3 = (C12-C21)/(4*beta0)
        elif beta12 == EP.max():
            beta1 = np.sqrt(beta12)
            beta0 = (C23-C32)/(4*beta1)
            beta2 = (C12-C21)/(4*beta1)
            beta3 = (C31+C13)/(4*beta1)
        elif beta22 == EP.max():
            beta2 = np.sqrt(beta22)
            beta0 = (C31-C13)/(4*beta2)
            beta1 = (C12+C21)/(4*beta2)
            beta3 = (C23+C32)/(4*beta2)
        else:
            beta3 = np.sqrt(beta32)
            beta0 = (C12-C21)/(4*beta3)
            beta1 = (C31+C13)/(4*beta3)
            beta2 = (C23+C32)/(4*beta3)
        beta = np.array([beta0, beta1, beta2, beta3])
        q = np.tan(np.deg2rad(float(Phi.get()))/2)*e
        sigma = np.tan(np.deg2rad(float((Phi.get())))/4)*e
        psi = np.rad2deg(np.arctan(C12/C11))
        theta = np.rad2deg(-1*np.arcsin(C13))
        phi = np.rad2deg(np.arctan(C23/C33))
        
        #sets
        euler_final.set("The Euler Angles is (" + str(round(psi,3)) + ", " +str(round(theta,3)) +", " +str(round(phi,3))+ ")")  
        beta_final.set("The quaternion is "+str(beta))
        q_final.set("The classical Rodrigues parameters is "+ str(q))
        sigma_final.set("The modifed Rodrigues parameters is " + str(sigma))
        
    #widgets
    label_e11 = Label(top3, font ='Arial 10', text='e1:')
    label_e12 = Label(top3, font ='Arial 10', text='e2:')
    label_e13 = Label(top3, font ='Arial 10', text='e3:')
    label_Phi = Label(top3, font ='Arial 10', text='Φ:')
    e11 = Entry(top3)
    e12 = Entry(top3)
    e13 = Entry(top3)
    Phi = Entry(top3)
    
    #layout
    label_e11.grid(row = 2, column =1)
    e11.grid(row=2, column =2)
    label_e12.grid(row=3,column=1)
    e12.grid(row=3,column=2)
    label_e13.grid(row=4, column=1)
    e13.grid(row=4,column=2)
    label_Phi.grid(row=5, column=1)
    Phi.grid(row=5,column=2)
    
    #focus
    e11.focus()
    
    #button
    btn5 = Button(top3,
                 text = "Calculate",
                 command = prv_calc
                 ).grid(row = 6, column = 2)
    
    #plots
    label_euler = Label(top3,textvariable=euler_final).grid(rowspan=6, column=1, stick =W)
    label_beta = Label(top3,textvariable=beta_final).grid(rowspan=6, column = 1, stick=W)
    label_q = Label(top3,textvariable=q_final).grid(rowspan=6, column = 1, stick=W)
    label_sigma = Label(top3,textvariable=sigma_final).grid(rowspan=6, column = 1, stick=W)
    
def command4():
    top4 = Toplevel()
    top4.title= ('Graphical User Interface for Attitude Coordinates of Satellites')
    top4.resizable(False, False)
    #top4.iconbitmap('@/home/geovani/Documentos/icon.xbm')   
    #altura e largura do programa
    largura = 860
    altura = 200
    
    #resolução
    largura_screen = top4.winfo_screenwidth()
    altura_screen = top4.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    top4.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    #definir como iconic
    top4.state('iconic')
    
    #definição das mensagens
    label_4 = Label(top4,
                    text = "Enter the CRP data:",
                    font = "Arial 11",
                    justify = LEFT
                    ).grid(row= 1, column = 1)
    
    #final
    phi_final = StringVar()
    e_final = StringVar()
    beta_final = StringVar()
    sigma_final = StringVar()
    euler_final = StringVar()
    
    #function
    def crp_calc():
        q = np.array([float(q1.get()), float(q2.get()), float(q3.get())])
        C11 = 1/(1+np.dot(q,q.T))*(1 + float(q1.get())**2-float(q2.get())**2-float(q3.get())**2)
        C12 = 1/(1+np.dot(q,q.T))*2*(float(q1.get())*float(q2.get())+float(q3.get()))
        C13 = 1/(1+np.dot(q,q.T))*2*(float(q1.get())*float(q3.get())-float(q2.get()))
        C21 = 1/(1+np.dot(q,q.T))*2*(float(q2.get())*float(q1.get())-float(q3.get()))
        C22 = 1/(1+np.dot(q,q.T))*(1 - float(q1.get())**2+float(q2.get())**2-float(q3.get())**2)
        C23 = 1/(1+np.dot(q,q.T))*2*(float(q2.get())*float(q3.get())+float(q1.get()))
        C31 = 1/(1+np.dot(q,q.T))*2*(float(q3.get())*float(q1.get())+float(q2.get()))
        C32 = 1/(1+np.dot(q,q.T))*2*(float(q3.get())*float(q2.get())-float(q1.get()))
        C33 = 1/(1+np.dot(q,q.T))*(1 - float(q1.get())**2-float(q2.get())**2+float(q3.get())**2)
        cos_Phi = 1/2*(C11+C22+C33-1)
        Phi = np.arccos(cos_Phi)
        Phideg = np.rad2deg(Phi)
        e11 = 1/(2*np.sin(Phi))*(C23-C32)
        e12 = 1/(2*np.sin(Phi))*(C31-C13)
        e13 = 1/(2*np.sin(Phi))*(C12-C21)
        e = np.array([e11,e12,e13])
        beta02 = 1/4*(1+C11+C22+C33)
        beta12 = 1/4*(1+2*C11-1*(C11+C22+C33))
        beta22 = 1/4*(1+2*C22-1*(C11+C22+C33))
        beta32 = 1/4*(1+2*C33-1*(C11+C22+C33))
        EP = np.array([beta02, beta12, beta22, beta32])
        EP.max()
        if beta02 == EP.max():
            beta0 = np.sqrt(beta02)
            beta1 = (C23-C32)/(4*beta0)
            beta2 = (C31-C13)/(4*beta0)
            beta3 = (C12-C21)/(4*beta0)
        elif beta12 == EP.max():
            beta1 = np.sqrt(beta12)
            beta0 = (C23-C32)/(4*beta1)
            beta2 = (C12-C21)/(4*beta1)
            beta3 = (C31+C13)/(4*beta1)
        elif beta22 == EP.max():
            beta2 = np.sqrt(beta22)
            beta0 = (C31-C13)/(4*beta2)
            beta1 = (C12+C21)/(4*beta2)
            beta3 = (C23+C32)/(4*beta2)
        else:
            beta3 = np.sqrt(beta32)
            beta0 = (C12-C21)/(4*beta3)
            beta1 = (C31+C13)/(4*beta3)
            beta2 = (C23+C32)/(4*beta3)
        beta = np.array([beta0, beta1, beta2, beta3])

        sigma = np.tan(Phi/4)*e
        psi = np.rad2deg(np.arctan(C12/C11))
        theta = np.rad2deg(-1*np.arcsin(C13))
        phi = np.rad2deg(np.arctan(C23/C33))
        
        #sets
        euler_final.set("The Euler Angles is (" + str(round(psi,3)) + ", " +str(round(theta,3)) +", " +str(round(phi,3))+ ")")  
        phi_final.set(r'The angle principal rotation vector is ' + str(round(Phideg,3)) + '°')
        e_final.set(r'The principal rotation vector is ' + str(e))
        beta_final.set("The quaternion is "+str(beta))
        sigma_final.set("The modified Rodrigues parameters is " + str(sigma))
        
        
    #widgets
    label_q1 = Label(top4, text='q_1:')
    label_q2 = Label(top4, text='q_2:')
    label_q3 = Label(top4, text='q_3:')
    q1 = Entry(top4)
    q2 = Entry(top4)
    q3 = Entry(top4)
    
    #layout
    label_q1.grid(row = 2, column =1)
    q1.grid(row=2, column =2)
    label_q2.grid(row=3,column=1)
    q2.grid(row=3,column=2)
    label_q3.grid(row=4, column=1)
    q3.grid(row=4,column=2)
    
    #focus
    q1.focus()
    
    #button
    btn5 = Button(top4,
                 text = "Calculate",
                 command = crp_calc
                 ).grid(row = 6, column = 2)
    
    #plots
    label_euler = Label(top4,textvariable=euler_final).grid(rowspan=6, column =1,stick=W)
    label_phi = Label(top4,textvariable=phi_final).grid(rowspan=6, column = 1, stick= W)
    label_e = Label(top4,textvariable=e_final).grid(rowspan=6, column = 1, stick=W)
    label_beta = Label(top4,textvariable=beta_final).grid(rowspan=6,column=1, stick = W)
    label_sigma = Label(top4,textvariable=sigma_final).grid(rowspan=6, column = 1, stick=W)
    
def command5():    
    top5 = Toplevel()
    top5.title= ('Graphical User Interface for Attitude Coordinates of Satellites')
    top5.resizable(False, False)
   # top5.iconbitmap('@/home/geovani/Documentos/icon.xbm')   
    #altura e largura do programa
    largura = 860
    altura = 200
    
    #resolução
    largura_screen = top5.winfo_screenwidth()
    altura_screen = top5.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    top5.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    #definir como iconic
    top5.state('iconic')
    
    #definição das mensagens
    label_5 = Label(top5,
                    text = "Enter the quaternion data:",
                    font = "Arial 11",
                    justify = LEFT
                    ).grid(row= 1, column = 1)
    
    #final
    phi_final = StringVar()
    e_final = StringVar()
    q_final = StringVar()
    sigma_final = StringVar()
    euler_final = StringVar()
    
    #function
    def qua_calc():
        C11 = float(beta0.get())**2+float(beta1.get())**2-float(beta2.get())**2-float(beta3.get())**2
        C12 = 2*(float(beta1.get())*float(beta2.get()) + float(beta0.get())*float(beta3.get()))
        C13 = 2*(float(beta1.get())*float(beta3.get()) - float(beta0.get())*float(beta2.get()))
        C21 = 2*(float(beta1.get())*float(beta2.get()) - float(beta0.get())*float(beta3.get()))
        C22 = float(beta0.get())**2-float(beta1.get())**2+float(beta2.get())**2-float(beta3.get())**2
        C23 = 2*(float(beta2.get())*float(beta3.get()) + float(beta0.get())*float(beta1.get()))
        C31 = 2*(float(beta1.get())*float(beta3.get()) + float(beta0.get())*float(beta2.get()))
        C32 = 2*(float(beta2.get())*float(beta3.get()) - float(beta0.get())*float(beta1.get()))
        C33 = float(beta0.get())**2-float(beta1.get())**2-float(beta2.get())**2+float(beta3.get())**2
        cos_Phi = 1/2*(C11+C22+C33-1)
        Phi = np.arccos(cos_Phi)
        Phideg = np.rad2deg(Phi)
        e11 = 1/(2*np.sin(Phi))*(C23-C32)
        e12 = 1/(2*np.sin(Phi))*(C31-C13)
        e13 = 1/(2*np.sin(Phi))*(C12-C21)
        e = np.array([e11,e12,e13])
        phi_final.set(r'The angle principal rotation vector is ' + str(round(Phideg,3)) + '°')
        e_final.set(r'The principal rotation vector is ' + str(e)) 
        q = np.tan(Phi/2)*e
        sigma = np.tan(Phi/4)*e
        q_final.set(r'The classical Rodrigues parameter is '+ str(q))
        sigma_final.set(r'The modifided Rodrigues parameter is ' + str(sigma))
        psi = np.rad2deg(np.arctan(C12/C11))
        theta = np.rad2deg(-1*np.arcsin(C13))
        phi = np.rad2deg(np.arctan(C23/C33))
        euler_final.set("The Euler Angles is (" + str(round(psi,3)) + ", " +str(round(theta,3)) +", " +str(round(phi,3))+ ")")  
        
    #widgets
    label_beta0 = Label(top5, font = "Arial 10", text='β_0:')
    label_beta1 = Label(top5, font = "Arial 10", text='β_1:')
    label_beta2 = Label(top5, font = "Arial 10", text='β_2:')
    label_beta3 = Label(top5, font = "Arial 10", text='β_3:')
    beta0 = Entry(top5)
    beta1 = Entry(top5)
    beta2 = Entry(top5)
    beta3 = Entry(top5)
    
    #layout
    label_beta0.grid(row = 2, column =1)
    beta0.grid(row=2, column =2)
    label_beta1.grid(row=3,column=1)
    beta1.grid(row=3,column=2)
    label_beta2.grid(row=4, column=1)
    beta2.grid(row=4,column=2)
    label_beta3.grid(row=5, column=1)
    beta3.grid(row=5,column=2)
    
    #focus
    beta0.focus()
    
    #button
    btn5 = Button(top5,
                 text = "Calculate",
                 command = qua_calc
                 ).grid(row = 6, column = 2)
    
    #plots
    label_euler = Label(top5,textvariable=euler_final).grid(rowspan=6, column=1, stick =W)
    label_phi = Label(top5,textvariable=phi_final).grid(rowspan=6, column = 1, stick= W)
    label_e = Label(top5,textvariable=e_final).grid(rowspan=6, column = 1, stick=W)
    label_q = Label(top5,textvariable=q_final).grid(rowspan=6, column = 1, stick=W)
    label_sigma = Label(top5,textvariable=sigma_final).grid(rowspan=6, column = 1, stick=W)
   
def command6():
    top6 = Toplevel()
    top6.title = ('Graphical User Interface for Attitude Coordinates of Satellites')
    top6.resizable(False, False)
    #top6.iconbitmap('@/home/geovani/Documentos/icon.xbm')   
    #altura e largura do programa
    largura = 860
    altura = 200
    
    #resolução
    largura_screen = top6.winfo_screenwidth()
    altura_screen = top6.winfo_screenheight()
    
    #posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    #definir a geometria
    top6.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    #definir como iconic
    top6.state('iconic')
    
    #definição das mensagens
    label_6 = Label(top6,
                    text = "Enter the MRP data:",
                    font = "Arial 11",
                    justify = LEFT
                    ).grid(row= 1, column = 1)

    #final 
    phi_final = StringVar()
    e_final = StringVar()
    beta_final = StringVar()
    q_final = StringVar()
    euler_final = StringVar()
    
    #function
    def mrp_calc(): 
        sigma = np.sqrt(float(sigma1.get())**2+float(sigma2.get())**2+float(sigma3.get())**2)
        c = 1/((1+sigma**2)**2)
        C11 = 1 - c*(8*(float(sigma2.get())**2+float(sigma3.get())**2))
        C12 = c*8*float(sigma1.get())*float(sigma2.get())+4*float(sigma3.get())*(1-sigma**2)
        C13 = c*8*float(sigma1.get())*float(sigma3.get())-4*float(sigma2.get())*(1-sigma**2)
        C21 = c*8*float(sigma2.get())*float(sigma1.get())-4*float(sigma3.get())*(1-sigma**2)
        C22 = 1 - c*(8*(float(sigma1.get())**2+float(sigma3.get())**2))
        C23 = c*8*float(sigma2.get())*float(sigma3.get())+4*float(sigma1.get())*(1-sigma**2)
        C31 = c*8*float(sigma3.get())*float(sigma1.get())+4*float(sigma2.get())*(1-sigma**2)
        C32 = c*8*float(sigma3.get())*float(sigma2.get())-4*float(sigma1.get())*(1-sigma**2)
        C33 = 1 - c*(8*(float(sigma1.get())**2+float(sigma2.get())**2))
        cos_Phi = 1/2*(C11+C22+C33-1)
        Phi = np.arccos(cos_Phi)
        Phideg = np.rad2deg(Phi)
        e11 = 1/(2*np.sin(Phi))*(C23-C32)
        e12 = 1/(2*np.sin(Phi))*(C31-C13)
        e13 = 1/(2*np.sin(Phi))*(C12-C21)
        e = np.array([e11,e12,e13])
        phi_final.set(r'The angle principal rotation vector is ' + str(round(Phideg,3)) + '°')
        e_final.set(r'The principal rotation vector is ' + str(e)) 
        beta02 = 1/4*(1+C11+C22+C33)
        beta12 = 1/4*(1+2*C11-1*(C11+C22+C33))
        beta22 = 1/4*(1+2*C22-1*(C11+C22+C33))
        beta32 = 1/4*(1+2*C33-1*(C11+C22+C33))
        EP = np.array([beta02, beta12, beta22, beta32])
        EP.max()
        if beta02 == EP.max():
            beta0 = np.sqrt(beta02)
            beta1 = (C23-C32)/(4*beta0)
            beta2 = (C31-C13)/(4*beta0)
            beta3 = (C12-C21)/(4*beta0)
        elif beta12 == EP.max():
            beta1 = np.sqrt(beta12)
            beta0 = (C23-C32)/(4*beta1)
            beta2 = (C12-C21)/(4*beta1)
            beta3 = (C31+C13)/(4*beta1)
        elif beta22 == EP.max():
            beta2 = np.sqrt(beta22)
            beta0 = (C31-C13)/(4*beta2)
            beta1 = (C12+C21)/(4*beta2)
            beta3 = (C23+C32)/(4*beta2)
        else:
            beta3 = np.sqrt(beta32)
            beta0 = (C12-C21)/(4*beta3)
            beta1 = (C31+C13)/(4*beta3)
            beta2 = (C23+C32)/(4*beta3)
        beta = np.array([beta0, beta1, beta2, beta3])
        beta_final.set("The quaternion is "+str(beta))
        q = np.tan(Phi/2)*e
        q_final.set("The classic Rodrigues parameters is "+ str(q))
        psi = np.rad2deg(np.arctan(C12/C11))
        theta = np.rad2deg(-1*np.arcsin(C13))
        phi = np.rad2deg(np.arctan(C23/C33))
        euler_final.set("The Euler Angles are (" + str(round(psi,3)) + ", " +str(round(theta,3)) +", " +str(round(phi,3))+ ")")  
        
        
        
        
    #widgets
    label_sigma1 = Label(top6, font = "Arial 10", text='σ_1:')
    label_sigma2 = Label(top6, font = "Arial 10", text='σ_2:')
    label_sigma3 = Label(top6, font = "Arial 10", text='σ_3:')
    sigma1 = Entry(top6)
    sigma2 = Entry(top6)
    sigma3 = Entry(top6)
    
    #layout
    label_sigma1.grid(row = 2, column =1)
    sigma1.grid(row=2, column =2)
    label_sigma2.grid(row=3,column=1)
    sigma2.grid(row=3,column=2)
    label_sigma3.grid(row=4, column=1)
    sigma3.grid(row=4,column=2)
    
    #focus
    sigma1.focus()
    
    #button
    btn5 = Button(top6,
                 text = "Calculate",
                 command = mrp_calc
                 ).grid(row = 6, column = 2)
    
    #plots
    labeL_euler = Label(top6,textvariable=euler_final).grid(rowspan=6,column=1, stick=W)
    label_phi = Label(top6,textvariable=phi_final).grid(rowspan=6, column = 1, stick= W)
    label_beta = Label(top6,textvariable=beta_final).grid(rowspan=6, column=1, stick= W)
    label_e = Label(top6,textvariable=e_final).grid(rowspan=6, column = 1, stick=W)
    label_q = Label(top6,textvariable=q_final).grid(rowspan=6, column = 1, stick=W)  

#definição das mensagens
helpb = Button(menu_inicial,
               text = "Help",
               command = helpc
               ).grid(rowspan = 1, column = 0, stick ='nw')

label_1 = Label(menu_inicial,
                text = "Hello, this is an algorithm developed by Geovani Augusto Xavier Ribeiro.",
                font = "Arial 10",
                bd = 5,
                relief = "ridge",
                padx = 2,
                pady = 2,
                justify = RIGHT,
                anchor = N
                ).grid(rowspan = 1, column = 0, stick = N)

label_2 = Label(menu_inicial,
                text = "You can calculate the main coordinate attitude with algorithm.\n First, is necessary to know some informations, click on the box with the information you have.",
                font = "Arial 11"
                ).grid(row =2, column = 0,stick=N)

#label_3 = Label(menu_inicial,
           #     text = "Geovani"
           #     ).grid(row=2, stick=SE)
                         
    
#botoes

cmd1 = Button(menu_inicial,
              text = "Directional Cosine Matrix",
              bg ="grey",
              bd = 3,
              relief = "ridge",
              command= command1 
              ).grid(rowspan = 3, column = 0, stick='nw')

cmd2 = Button(menu_inicial,
              text = "Euler Angles",
              bg ="grey",
              bd = 3,
              relief = "ridge",
              command=command2
              ).grid(row = 3, column =0)

cmd3 = Button(menu_inicial,
              text = "Principal Rotation Vector",
              bg ="grey",
              bd = 3,
              relief = "ridge",
              command= command3
              ).grid(row = 3, column =0, stick ='se')

cmd4 = Button(menu_inicial,
              text = "Classical Rodrigues Parameters",
              bg ="grey",
              bd = 3,
              relief = "ridge",
              command= command4
              ).grid(row = 4, column =0, stick='sw')

cmd5 = Button(menu_inicial,
              text = "Quaternions",
              bg ="grey",
              bd = 3,
              relief = "ridge",
              command = command5
              ).grid(row = 4, column =0)

cmd6 = Button(menu_inicial,
              text = "Modified Rodrigues Parameters",
              bg ="grey",
              bd = 3,
              relief = "ridge",
              command= command6
              ).grid(row = 4, column =0, stick ='se')





#loop
menu_inicial.mainloop()