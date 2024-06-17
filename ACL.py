import customtkinter as ctk
import tkinter as tk
import subprocess
import os
import re
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog


class ACLManager:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.h_command = []
        

    def print_acl(self):
        f = self.file_combobox.get()  
        if not f.strip():
            self.rules_listbox.insert(tk.END, "Inserisci un nome di file valido.")
            return

        try:
            command = ["getfacl", f]
            result = subprocess.run(command, capture_output=True, text=True)
            self.h_command.append(command)
            print(self.h_command)
            output = result.stdout

            if result.returncode == 0:
                self.rules_listbox.delete(0, tk.END)
            
                for line in output.splitlines():
                    self.rules_listbox.insert(tk.END, line)
            else:
                self.rules_listbox.insert(tk.END, f"Errore nell'esecuzione di getfacl: {result.stderr}")

        except Exception as e:
            self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")

    def select_user(self):
        user = self.entry_user.get()
        print(user)
        return user
    
    def select_file(self):
        file = self.file_combobox.get()
        print(file)
        return file
    
    def select_group(self):
        group = self.entry_group.get()
        print(group)
        return group
    
    #User : antrunieddru,dio,pietro,giacomo
    def update_permissions(self):
        file = self.file_combobox.get()
        user = self.entry_user.get()
        if not file.strip():
            self.rules_listbox.insert(tk.END, "Seleziona un file valido.")
            return
        else:
            try:
                if self.perm_choice.get()==1:
                    command = ["setfacl","-m",f"u:{user}:r--",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(self.h_command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==2:
                    command=["setfacl","-m",f"u:{user}:--w",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(self.h_command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)
                
                if self.perm_choice.get()==3:
                    command=["setfacl","-m",f"u:{user}:--x",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(self.h_command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==4:
                    command= ["setfacl","-m",f"u:{user}:rwx",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==5:
                    command=["setfacl","-x",f"u:{user}",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(self.h_command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

            except Exception as e:
                self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")


    def update_mask(self):
        file = self.file_combobox.get()
        if not file.strip():
            self.rules_listbox.insert(tk.END, "Seleziona un file valido.")
            return
        else:
            try:
                if self.perm_choice.get()==1:
                    command = ["setfacl","-m","m:r--",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==2:
                    command = ["setfacl","-m","m:-w-",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)
                
                if self.perm_choice.get()==3:
                    command = ["setfacl","-m","m:--x",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==4:
                    command = ["setfacl","-m","m:rwx",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==5:
                    CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando", icon="cancel", master=root)

            except Exception as e:
                self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")

    #Gruppi lab,lab1
    def update_group(self):
        file = self.file_combobox.get()
        group = self.entry_group.get()
        if not file.strip():
            self.rules_listbox.insert(tk.END, "Seleziona un file valido.")
            return
        else:
            try:
                if self.perm_choice.get()==1:
                    command = ["setfacl","-m",f"g:{group}:r--",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==2:
                    command = ["setfacl","-m",f"g:{group}:--w",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)
                
                if self.perm_choice.get()==3:
                    command = ["setfacl","-m",f"g:{group}:--x",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==4:
                    command = ["setfacl","-m",f"g:{group}:rwx",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==5:
                    command = ["setfacl","-x",f"g:{group}",file]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

            except Exception as e:
                self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")

    def update_dir(self):    
        dir = self.dir_selezionata
        user = self.entry_user.get()
        try:
                if self.perm_choice.get()==1:
                    command = ["setfacl","-m",f"d:u:{user}:r--",dir]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==2:
                    command = ["setfacl","-m",f"d:u:{user}:w--",dir]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)
                
                if self.perm_choice.get()==3:
                    command = ["setfacl","-m",f"d:u:{user}:--x",dir]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==4:
                    command = ["setfacl","-m",f"d:u:{user}:rwx",dir]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

                if self.perm_choice.get()==5:
                    command = ["setfacl","-b",dir]
                    result = subprocess.run(command, capture_output=True, text=True)
                    output = result.stdout
                    self.h_command.append(command)
                    print(command)

                    if result.returncode == 0:
                        self.rules_listbox.delete(0, tk.END)
                        CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
                    else:
                        CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

        except Exception as e:
                self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")

    def rm_def(self):
        
        dir = self.dir_selezionata
        command = ["setfacl","-k",dir]
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            output = result.stdout

            if result.returncode == 0:
                self.rules_listbox.delete(0, tk.END)
                CTkMessagebox(title="Successo", message="Azione avvenuta con successo.", icon="check", master=root)
            else:
                CTkMessagebox(title="Errore", message=f"Errore nell'esecuzione del comando: {result.stderr}", icon="cancel", master=root)

        except Exception as e:
                self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")

   
    def stmp_command(self):
        commands = self.h_command
        #last_commands = commands[-5] #possono essere gli ultimi 5/10
        self.rules_listbox.delete(0, tk.END)
        for c in commands:
            self.rules_listbox.insert(tk.END, c)
            print(" ".join(c))


    def print_dir(self):
        dir = self.dir_selezionata
        print(dir)
        try:
            command = ["getfacl", dir]
            result = subprocess.run(command, capture_output=True, text=True)
            self.h_command.append(command)
            print(self.h_command)
            output = result.stdout

            if result.returncode == 0:
                self.rules_listbox.delete(0, tk.END)
            
                for line in output.splitlines():
                    self.rules_listbox.insert(tk.END, line)
            else:
                self.rules_listbox.insert(tk.END, f"Errore nell'esecuzione di getfacl: {result.stderr}")

        except Exception as e:
            self.rules_listbox.insert(tk.END, f"Errore durante l'esecuzione del comando: {str(e)}")

    def seleziona_dir(self):
        self.dir_selezionata = filedialog.askdirectory()
        if self.dir_selezionata:
            print("Directory selezionata:", self.dir_selezionata)
            self.select_dir.configure(text=f"Directory selezionata: {self.dir_selezionata}")
            #return self.dir_selezionata
        
    def mostra_file(self):
        dir = self.dir_selezionata
        try:
            file_l = os.listdir(dir)
            file_list=[f for f in file_l if os.path.isfile(os.path.join(dir, f))]

            if file_list:
                self.file_combobox.configure(values=file_list)
                self.file_combobox.set(file_list[0])
            else:
                self.file_combobox.configure(values=["Nessun file trovato"])
                self.file_combobox.set(file_list[0])

        except Exception as e:
            self.file_combobox.configure(values=[f"Errore : {str(e)}"])
            self.file_combobox.set(f"Errore: {str(e)}")
        
    

    def setup_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        frame = ctk.CTkFrame(self.root, width=300, height=200)
        frame.pack(pady=20)

        label_file = ctk.CTkLabel(frame, text="Scegli un file:")
        label_file.grid(row=1, column=0, padx=5, pady=5)

        #current_files = os.listdir('.')
        self.file_combobox = ctk.CTkComboBox(frame, values=["Nessun file selezionato"], width=200)
        self.file_combobox.grid(row=1, column=1, padx=5, pady=5)

        cnf_file = ctk.CTkButton(frame, text="Visualizza permessi:", command=self.print_acl)
        cnf_file.grid(row=1, column=3, padx=5, pady=10)

        btn_file = ctk.CTkButton(frame, text="Trova file:",command=self.mostra_file)
        btn_file.grid(row=1, column=2 ,padx=5, pady=10)


        label_user = ctk.CTkLabel(frame , text="Seleziona Utente:")
        label_user.grid(row=2, column=0, padx=5, pady=5)

        self.entry_user = ctk.CTkEntry(frame, width=200)
        self.entry_user.grid(row=2, column=1, padx=5, pady=5)

        btn_user = ctk.CTkButton(frame, text="Seleziona", command=self.select_user)
        btn_user.grid(row=2, column=3, padx=5, pady=10)


        label_group = ctk.CTkLabel(frame , text="Seleziona Gruppo:")
        label_group.grid(row=3, column=0, padx=5, pady=5)

        self.entry_group = ctk.CTkEntry(frame, width=200)
        self.entry_group.grid(row=3, column=1, padx=5, pady=5)

        btn_group = ctk.CTkButton(frame, text="Seleziona", command=self.select_group)
        btn_group.grid(row=3, column=3, padx=5, pady=10)

        self.perm_choice = tk.IntVar(value=0)  

        label_perm = ctk.CTkLabel(frame, text="Imposta permessi:")
        label_perm.grid(row=4, column=0, padx=5, pady=5)

        perm_read = ctk.CTkRadioButton(frame, text="Lettura", variable=self.perm_choice, value=1)
        perm_read.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        perm_write = ctk.CTkRadioButton(frame, text="Scrittura", variable=self.perm_choice, value=2)
        perm_write.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

        perm_exec = ctk.CTkRadioButton(frame, text="Esecuzione", variable=self.perm_choice, value=3)
        perm_exec.grid(row=4, column=3, padx=5, pady=5, sticky="ew")

        tot_perm = ctk.CTkRadioButton(frame, text="Imposta tutti", variable=self.perm_choice, value=4)
        tot_perm.grid(row=4, column=4, padx=5, pady=5, sticky="ew")

        rim_perm = ctk.CTkRadioButton(frame, text="Rimuovi", variable=self.perm_choice, value=5)
        rim_perm.grid(row=4, column=5, padx=5, pady=5, sticky="ew")

        apply_btn = ctk.CTkButton(frame, text="Applica Permesso Utente", command=self.update_permissions)
        apply_btn.grid(row=6, column=1,columnspan=2, padx=5, pady=10)

        mask_btn = ctk.CTkButton(frame,text="Applica Permesso Maschera", command=self.update_mask)
        mask_btn.grid(row=6, column=2,columnspan=2,padx=5, pady=10)

        grp_btn = ctk.CTkButton(frame,text="Applica Permesso Gruppo", command=self.update_group)
        grp_btn.grid(row=6, column=3,columnspan=3,padx=5, pady=10)

        dir_btn = ctk.CTkButton(frame, text="Modifica Permessi Current Directory", command=self.update_dir)
        dir_btn.grid(row=7,column=1,columnspan=1,padx=5,pady=10)

        rm_btn= ctk.CTkButton(frame, text="Rimuovere Permesso Default Current Directory",command=self.rm_def)
        rm_btn.grid(row=7,column=2,columnspan=2,padx=5,pady=10)

        mst_btn= ctk.CTkButton(frame, text="Mostra Permessi Current Directory",command=self.print_dir)
        mst_btn.grid(row=7,column=4,columnspan=3,padx=5,pady=10)

        #rec_btn= ctk.CTkButton(frame, text="Gestione Ricorsiva ACL",command=self.update_rec)
        #rec_btn.grid(row=7,column=1,columnspan=2,padx=5,pady=10)

        stp_btn= ctk.CTkButton(frame, text="Stampa comandi eseguiti",command=self.stmp_command)
        stp_btn.grid(row=8,column=2 ,columnspan=2,padx=5,pady=10)

        #dir_selezionata = filedialog.askdirectory()
        self.select_dir = ctk.CTkLabel(frame, text="Nessuna directory selezionata")
        self.select_dir.grid(row=9,column=2,columnspan=2,padx=5,pady=5)

        self.btn_select= ctk.CTkButton(frame, text="Seleziona Directory",command=self.seleziona_dir)
        self.btn_select.grid(row=1,column=4,padx=5,pady=5)

        self.rules_listbox = tk.Listbox(self.root, height=15, width=80)
        self.rules_listbox.pack(pady=20)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("ACL Manager")

    app = ACLManager(root)
    app.start()
