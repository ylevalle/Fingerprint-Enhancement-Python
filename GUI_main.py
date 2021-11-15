#! ./env/bin/python
import os
import subprocess
from os.path import join

import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog

from main_enhancement import ROOT, IMG_FORMATS, SUFFIX, image_enhance_from

COLORS = {
    'primary': '#1976D2',
    'secondary': '#424242',
    'accent': '#82B1FF',
    'error': '#FF5252',
    'info': '#2196F3',
    'success': '#4CAF50',
    'warning': '#FFC107'
}


class FingerprintImgEnhancer:
    def __init__(self, master: Tk, title: str) -> None:
        self.master = master
        self.master.title(title)
        # properties
        self.inp_folder = 'images'
        self.tar_folder = 'enhanced'
        # labels
        Label(
            master=self.master,
            text='Esta es una aplicacion para mejorar imagenes de huellas digitales').pack(pady=5)
        Label(self.master, text='Imagenes seleccionadas').pack(pady=2)
        # list box
        self.dir_list_box = Listbox(self.master)
        self.dir_list_box.pack(fill='x', padx=100)
        # butons
        self.select_dir_b = Button(
            master=self.master,
            text='Selecciona un directorio',
            command=self.select_directory)
        self.select_dir_b.pack(pady=5)
        Button(
            master=self.master,
            text='Abrir carpeta destino',
            command=self.open_enhance_dir
        ).pack(pady=5)
        self.enhace_b = Button(
            master=self.master,
            text='Mejorar!',
            command=self.start_enhance)
        self.enhace_b.pack(fill=None, anchor="s",
                           side="left", padx=30, pady=30)
        self.enhace_b['state'] = 'normal' if self.update_dir_list(
            self.inp_folder) else 'disable'
        self.exit_b = Button(
            master=self.master,
            bg=COLORS['error'],
            text='Salir',
            command=self.master.quit)
        self.exit_b.pack(fill=None, anchor="s",
                         side="right", padx=30, pady=30)

    def select_directory(self):
        inp_folder = filedialog.askdirectory()
        self.inp_folder = inp_folder if inp_folder else self.inp_folder
        self.enhace_b['state'] = 'normal' if self.update_dir_list(
            self.inp_folder) else 'disable'

    def update_dir_list(self, inp_folder) -> bool:
        self.files = [
            filename for filename in os.listdir(inp_folder) if filename.split('.')[-1] in IMG_FORMATS]
        self.dir_list_box.delete(0, 'end')
        for i, filename in enumerate(self.files):
            self.dir_list_box.insert(i+1, filename)
        self.dir_list_box.update()
        return bool(self.files)

    def start_enhance(self):
        dialog = EnhancerDialog(
            self, self.master, 'Progress',
            message='¿Desea mejorar estas imagenes?')
        dialog.minsize(width=340, height=80)

    def open_enhance_dir(self):
        try:
            subprocess.run(['open', 'enhanced'], check=True)
        except Exception as e:
            print(e)
            try:
                subprocess.run(['open', 'enhanced'], check=True)
            except Exception as e:
                print(e)


class EnhancerDialog(Toplevel):
    def __init__(self, app: FingerprintImgEnhancer, master: Tk, title: str, message):
        super().__init__(master)
        # properties
        self.app = app
        self.title(title)
        self.wm_attributes("-type", "dialog")
        self.text = tk.StringVar()
        self.text.set(message)
        self.label = Label(self, textvariable=self.text)
        self.label.pack(padx=10, pady=10)
        # progress bar
        self.progbar = ttk.Progressbar(
            self, orient=HORIZONTAL, length=300, mode='determinate')
        self.progbar.pack(pady=2)
        # buttoms
        self.frame = Frame(self)
        self.frame.pack(side='bottom')
        self.start_b = Button(
            master=self.frame,
            text='Iniciar',
            bg=COLORS['primary'],
            command=self.start)
        self.start_b.pack(fill='y', anchor="s", side='left')
        self.cancel_b = Button(
            master=self.frame,
            text='Cancel',
            bg=COLORS['error'],
            command=self.__cancel)
        self.cancel_b.pack(fill='y', anchor="s", side='left')

    def start(self):
        self.__disable_buttoms()
        self.master.update
        self.update
        step_size = 100 / len(self.app.files)
        for img_name in self.app.files:
            self.__update_dialog(img_name)
            enhanced_img = image_enhance_from(
                join(self.app.inp_folder, img_name))
            enhanced_img_name = img_name.split('.')
            enhanced_img_name = enhanced_img_name[0] + \
                SUFFIX + enhanced_img_name[-1]
            cv2.imwrite(join(self.app.tar_folder,
                        enhanced_img_name), enhanced_img)
            self.__update_dialog(img_name)
            self.progbar['value'] += step_size
        self.__normal_buttoms()
        self.text.set('Imagenes transformadas exitosamente.')
        self.start_b.destroy()
        self.cancel_b.destroy()
        Button(
            master=self.frame, text='Ok!',
            command=self.destroy, padx=20
        ).pack(fill='y', anchor="s", side='left')
        self.update()

    def __disable_buttoms(self):
        self.app.enhace_b['state'] = 'disable'
        self.app.exit_b['state'] = 'disable'
        self.app.select_dir_b['state'] = 'disable'
        self.start_b['state'] = 'disable'
        #self.cancel_b['state'] = 'disable'

    def __normal_buttoms(self):
        self.app.enhace_b['state'] = 'normal'
        self.app.exit_b['state'] = 'normal'
        self.app.select_dir_b['state'] = 'normal'
        self.start_b['state'] = 'normal'
        #self.cancel_b['state'] = 'normal'

    def __update_dialog(self, img_name):
        text_filename = f'{img_name[:10]}...' if len(
            img_name) > 10 else img_name
        self.text.set(f'Imagen: {text_filename:15} en progreso')
        self.master.update()
        self.update()

    def __cancel(self):
        self.__normal_buttoms()
        self.update
        self.master.update
        self.destroy()


if __name__ == '__main__':
    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('enhanced'):
        os.mkdir('enhanced')
    root = Tk()
    root.minsize(width=600, height=440)
    root.maxsize(width=600, height=440)
    root.geometry('540x360')
    feapp = FingerprintImgEnhancer(root, 'Fingerprint enhancer')
    root.mainloop()
