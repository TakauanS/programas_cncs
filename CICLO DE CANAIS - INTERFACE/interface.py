import customtkinter as ctk
from ciclo_canais import CicloCanal
from tkinter import messagebox
from PIL import Image

class Interface(ctk.CTk):

    cor1 = '#7CB8F2' # COR AZUL - FRACA
    cor2 = '#FEFAF1' # COR BRANCA
    cor3 = '#4675C0' # COR AZUL - FORTE

    def __init__(self):
        super().__init__()

        self.title('Ciclo de Canal - Parametric')
        self.resizable(width=False, height=False)
        self.config(background=Interface.cor1)
        self.geometry('595x380')
        self.iconbitmap('C:/Users/USUARIO/Documents/Programas CNCs/CICLO DE CANAIS - INTERFACE/imgs/favicon.ico')

        def seguir_campos():
            ciclo_tabview.set('PARÂMETROS DE CORTE')

        def voltar_campos():
            ciclo_tabview.set('PARÂMETROS DE CICLO')

        def code():

            # SEÇÃO DE CONVERSÃO DE GETs

            d_inicial = float(entry_diametroi.get())
            d_final = float(entry_diametrof.get())
            n_canais = int(entry_ncanais.get())
            pos_canais = entry_pos.get()

            ferramenta = str(entry_ferramenta.get())
            avanco = float(entry_avanco.get())
            rpm = float(entry_rotacao.get())
            ref = ref_combobox.get()

            # SEÇÃO DE EXCEPTION

            if d_inicial < d_final:
                msg = messagebox.showerror(title='Ciclo de Canal - Parametric', 
                                          message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, revise os valores e tente novamente.')

                entry_diametroi.delete(0, 100)
                entry_diametrof.delete(0, 100)

            if n_canais <= 0:
                msg = messagebox.showerror(title='Ciclo de Canais - Parametric',
                                           message='O número de canais não pode ser zero ou negativo. Por favor, insira um valor válido.')
                
                entry_ncanais.delete(0, 100)

            if avanco <= 0:
                msg = messagebox.showerror(title='Ciclo de Canais - Parametric',
                                           message='O valor do avanço não pode ser negativo. Por favor, insira um valor válido.')

                entry_avanco.delete(0, 100)

            if rpm <=0:
                msg = messagebox.showerror(title='Ciclo de Canais',
                                           message='O valor do RPM deve ser maior que zero. Por favor, insira um valor válido.')
                
                entry_rotacao.delete(0, 100)

            else:
                msg = messagebox.showinfo(title='Ciclo de Canais - Parametric',
                                          message='Os dados foram salvos com sucesso e o ciclo de canal foi compilado com sucesso.')

            # SEÇÃO DE CICLO DE CANAIs

            ciclo_canal = CicloCanal(diametro_inicial=d_inicial, diametro_final=d_final, n_canais=n_canais, pos_canais=pos_canais)

            ciclo_canal.referencia_trabalho(ref=ref)
            ciclo_canal.ferramenta(tool=ferramenta)
            ciclo_canal.avanco(advance=avanco)
            ciclo_canal.rotacao(rpm=rpm)

            ciclo_canal.gcode()

        # SEÇÃO DE EXPORTAÇÃO DE IMAGENs

        img_direita = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Programas CNCs/CICLO DE CANAIS - INTERFACE/imgs/seta_esquerda.png'), size=(24, 24))
        img_seguir = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Programas CNCs/CICLO DE CANAIS - INTERFACE/imgs/seta_direita.png'), size=(24, 24))
        img_code = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Programas CNCs/CICLO DE CANAIS - INTERFACE/imgs/code.png'), size=(24, 24))

        # SEÇÃO DE FRAMEs 

        ciclo_tabview = ctk.CTkTabview(master=self, corner_radius=10, width=575, height=370, bg_color=Interface.cor1, fg_color=Interface.cor2, state='disabled')
        ciclo_tabview.place(x=10, y=0)

        aba_parametros = ciclo_tabview.add('PARÂMETROS DE CICLO')
        aba_corte = ciclo_tabview.add('PARÂMETROS DE CORTE')

        # SEÇÃO DE LABELs

        label_diametroi = ctk.CTkLabel(master=aba_parametros, text='Ø DIÂMETRO INICIAL', font=('Corbel', 22))
        label_diametroi.place(x=15, y=10)

        label_diametrof = ctk.CTkLabel(master=aba_parametros, text='Ø DIÂMETRO FINAL', font=('Corbel', 22))
        label_diametrof.place(x=350, y=10)

        label_ncanais = ctk.CTkLabel(master=aba_parametros, text='NÚMERO DE CANAIS', font=('Corbel', 22))
        label_ncanais.place(x=15, y=95)

        label_pos = ctk.CTkLabel(master=aba_parametros, text='POS. DOS CANAIS', font=('Corbel', 22))
        label_pos.place(x=350, y=95)

        label_ferramenta = ctk.CTkLabel(master=aba_corte, text='FERRAMENTA', font=('Corbel', 22))
        label_ferramenta.place(x=15, y=10)

        label_avanco = ctk.CTkLabel(master=aba_corte, text='AVANÇO', font=('Corbel', 22))
        label_avanco.place(x=350, y=10)

        label_rotacao = ctk.CTkLabel(master=aba_corte, text='ROTAÇÃO', font=('Corbel', 22))
        label_rotacao.place(x=15, y=95)

        label_referencia = ctk.CTkLabel(master=aba_corte, text='REFERÊNCIA', font=('Corbel', 22))
        label_referencia.place(x=350, y=95)

        # SEÇÃO DE ENTRYs

        entry_diametroi = ctk.CTkEntry(master=aba_parametros, corner_radius=10, width=195)
        entry_diametroi.place(x=15, y=45)

        entry_diametrof = ctk.CTkEntry(master=aba_parametros, corner_radius=10, width=195)
        entry_diametrof.place(x=350, y=45)

        entry_ncanais = ctk.CTkEntry(master=aba_parametros, corner_radius=10, width=195)
        entry_ncanais.place(x=15, y=130)

        entry_pos = ctk.CTkEntry(master=aba_parametros, corner_radius=10, width=195)
        entry_pos.place(x=350, y=130)

        entry_ferramenta = ctk.CTkEntry(master=aba_corte, corner_radius=10, width=195)
        entry_ferramenta.place(x=15, y=45)

        entry_avanco = ctk.CTkEntry(master=aba_corte, corner_radius=10, width=195)
        entry_avanco.place(x=350, y=45)

        entry_rotacao = ctk.CTkEntry(master=aba_corte, corner_radius=10, width=195)
        entry_rotacao.place(x=15, y=130)

        # SEÇÃO DE COMBOBOX

        ref_values = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59']

        ref_combobox = ctk.CTkComboBox(master=aba_corte, 
                                        corner_radius=10, 
                                        values=ref_values,
                                        button_color=Interface.cor1,
                                        state='readonly', 
                                        width=195)
        ref_combobox.place(x=350, y=130)
        ref_combobox.set('')

        # SEÇÃO DE BUTTONs

        button_seguir = ctk.CTkButton(master=aba_parametros,
                                      image=img_seguir,
                                      command=seguir_campos,
                                      compound='right', 
                                      corner_radius=10, 
                                      text='SEGUIR', 
                                      border_width=1,
                                      width=120, 
                                      font=('Corbel', 16, 'bold'), 
                                      fg_color=Interface.cor2, 
                                      text_color=Interface.cor3,
                                      border_color=Interface.cor3,
                                      hover_color=Interface.cor1)
        button_seguir.place(x=430, y=280)

        button_code = ctk.CTkButton(master=aba_corte,
                                    image=img_code,
                                    command=code,
                                    compound='left', 
                                    corner_radius=10, 
                                    text='G-CODE', 
                                    border_width=1,
                                    width=120, 
                                    font=('Corbel', 16, 'bold'), 
                                    fg_color=Interface.cor2, 
                                    text_color=Interface.cor3,
                                    border_color=Interface.cor3,
                                    hover_color=Interface.cor1)
        button_code.place(x=430, y=280)

        button_voltar = ctk.CTkButton(master=aba_corte,
                                    image=img_direita,
                                    command=voltar_campos,
                                    compound='left', 
                                    corner_radius=10, 
                                    text='VOLTAR', 
                                    border_width=1,
                                    width=120, 
                                    font=('Corbel', 16, 'bold'), 
                                    fg_color=Interface.cor2, 
                                    text_color=Interface.cor3,
                                    border_color=Interface.cor3,
                                    hover_color=Interface.cor1)
        button_voltar.place(x=5, y=280)

        # SEÇÃO DE DEFs

        self.mainloop()