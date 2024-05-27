import tkinter as tk
import directory

class terminal:

    def __init__(self):
        #Variables logicas
        self.actualRow = 1
        self.actualDirectory = directory.Directory("Root")
        self.path = ""

        #Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Terminal")
        self.ventana.geometry("1000x800")
        self.ventana.grid_rowconfigure("all", pad=0)
        self.ventana.grid_columnconfigure("all", pad=0)
        self.helpLable = tk.Label(self.ventana, text="Type'help' for a list of commands", bg="blue",fg="white")
        self.helpLable.grid(row = 0, column = 0, sticky="ew")
        self.label1 = tk.Label(self.ventana, text="LastCommand", bg="yellow")
        self.label1.grid(row = 0, column = 3, sticky="ew")
        self.label2 = tk.Label(self.ventana, text="OutPut", bg="green")
        self.label2.grid(row = 0, column = 4, sticky="ew")

        #Inputs Usuario
        self.commandLine = tk.Text(self.ventana, height=1, width=1)
        self.commandLine.grid(row = self.actualRow, column = 1, sticky="nsew")
        self.commandLine.bind("<Return>", self.ejecutarComando)
        self.commandLine.bind("<KeyRelease>", self.modificarAnchoTextBox)
        self.commandLine.bind("<Tab>", self.autoCompletar)


        #Label Static Text
        self.actualDirectoryLabel = tk.Label(self.ventana, text=self.actualDirectory.path + ">", padx=0, pady=0)
        self.actualDirectoryLabel.grid(row = self.actualRow, column = 0, sticky="nsew")



        self.ventana.mainloop()

    def modificarAnchoTextBox(self, event):
        self.commandLine.config(width=len(self.commandLine.get("1.0", tk.END)))


    def ejecutarComando(self, event=None):

        userInput = self.commandLine.get("1.0", tk.END)

        comando = userInput.split(" ")[0].strip()

        if comando == "cls":
            self.crearVentana()
            return

        if comando == "exit":
            self.ventana.destroy()
            return
        
        if comando == "help":
            self.commandOutPut("Comandos disponibles: dir, mkdir, cd, actual, addfile, rm")
            return

        if comando == "dir":
            directorios = ""
            archivos = ""
            for subDirectory in self.actualDirectory.subDirectories:
                directorios = "-<DIR>" + subDirectory.directoryName +" "+ directorios
            for file in self.actualDirectory.files:
                archivos = "-<FILE>" + file + " " + archivos
            self.commandOutPut(directorios + " " +archivos)
            return

        try:
            argumento = userInput.split(maxsplit=1)[1].strip()
        except IndexError:
            self.commandOutPut("Missing argument")
            return


        if comando == "mkdir":
            createdDirectory = self.actualDirectory.makeDirectory(argumento)
            if createdDirectory is None:
                self.commandOutPut("Error: Directory already exists")
            else: 
                self.actualDirectory = createdDirectory
                self.commandOutPut(f"Directory {createdDirectory.directoryName} created")
                
        elif comando == "cd":
            targetDirectory = self.actualDirectory.changeDirectory(argumento)
            if targetDirectory is None:
                self.commandOutPut("Error: Directory does not exist")
            else:
                self.actualDirectory = targetDirectory
                self.commandOutPut(f"Changed to directory {targetDirectory.directoryName}")
 
        elif comando == "actual":
            self.commandOutPut("Directorio actual: " + self.actualDirectory.directoryName)
        elif comando == "addfile":
            self.actualDirectory.createFile(argumento)
            self.commandOutPut(f"Archivo {argumento} creado")
        elif comando == "rm":
            if self.actualDirectory.remove(argumento):
                self.commandOutPut(f"Removed {argumento}")
            else:
                self.commandOutPut("Error: File or directory not found")
        else:
            self.commandOutPut("Error: Command not found")
        
        
    def autoCompletar(self, event=None):

        texto = self.commandLine.get("1.0", tk.END).strip()
        partes = texto.split(" ")
        parteIncompleta = texto.split(maxsplit=1)[1].strip()
        print(parteIncompleta)

        directoryName = self.actualDirectory.autoComplete(parteIncompleta)

        print(directoryName)
        if directoryName is None:
            return 

        textoNuevo = partes[0] + " " + directoryName.strip()

        self.commandLine.delete("1.0", tk.END)
        self.commandLine.insert("1.0", textoNuevo)


    def commandOutPut(self, message):

        self.actualRow += 2

        lastCommand = self.actualDirectoryLabel.cget("text") + " " +self.commandLine.get("1.0", tk.END) 
        
        lastCommandLabel = tk.Label(self.ventana, text=lastCommand, width=len(lastCommand), bg="yellow")
        lastCommandLabel.grid(row = self.actualRow-2, column = 0, sticky="ew")

        outputLabel = tk.Label(self.ventana, text=message, width=len(message), bg="green")
        outputLabel.grid(row = self.actualRow-1, column = 0, sticky="ew")

        self.actualDirectoryLabel.grid(row = self.actualRow, column = 0)
        self.commandLine.grid(row = self.actualRow, column = 1)

        self.actualDirectoryLabel.config(text=self.actualDirectory.path + ">", width=len(self.actualDirectory.path + ">"))
        self.commandLine.delete("1.0", tk.END)
    
    def crearVentana(self):
        self.ventana.destroy()
        self.ventana = tk.Tk()
        self.ventana.title("Terminal")
        self.ventana.geometry("1000x800")
        self.ventana.grid_rowconfigure("all", pad=0)
        self.ventana.grid_columnconfigure("all", pad=0)
        self.helpLable = tk.Label(self.ventana, text="Type'help' for a list of commands", bg="blue",fg="white")
        self.helpLable.grid(row = 0, column = 0, sticky="ew")
        self.label1 = tk.Label(self.ventana, text="LastCommand", bg="yellow")
        self.label1.grid(row = 0, column = 3, sticky="ew")
        self.label2 = tk.Label(self.ventana, text="OutPut", bg="green")
        self.label2.grid(row = 0, column = 4, sticky="ew")

        #Inputs Usuario
        self.commandLine = tk.Text(self.ventana, height=1, width=1)
        self.commandLine.grid(row = self.actualRow, column = 1, sticky="nsew")
        self.commandLine.bind("<Return>", self.ejecutarComando)
        self.commandLine.bind("<KeyRelease>", self.modificarAnchoTextBox)
        self.commandLine.bind("<Tab>", self.autoCompletar)


        #Label Static Text
        self.actualDirectoryLabel = tk.Label(self.ventana, text=self.actualDirectory.path + ">", padx=0, pady=0)
        self.actualDirectoryLabel.grid(row = self.actualRow, column = 0, sticky="nsew")
        


terminal()




