from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from database import Database

db = Database()

class MenuScreen(Screen):
    pass

class AddClienteScreen(Screen):
    def add_cliente(self, nome, telefone, procedimento, valor_pago, metodo_pagamento, lucro):
        db.add_cliente(nome, telefone, procedimento, float(valor_pago), metodo_pagamento, float(lucro))
        self.manager.current = 'menu'

class ListClienteScreen(Screen):
    def on_enter(self):
        clientes = db.list_clientes()
        self.ids.cliente_list.clear_widgets()
        for cliente in clientes:
            self.ids.cliente_list.add_widget(Label(text=f"{cliente[0]} - {cliente[1]} - {cliente[2]} - {cliente[3]} - R$ {cliente[4]} - {cliente[5]} - R$ {cliente[6]}"))

class DeleteClienteScreen(Screen):
    def delete_cliente(self, cliente_id):
        db.delete_cliente(int(cliente_id))
        self.manager.current = 'menu'

class ProfitScreen(Screen):
    def calculate_lucro(self, data_inicio, data_fim):
        lucro = db.calculate_lucro(data_inicio, data_fim)
        self.ids.lucro_result.text = f'Lucro: R$ {lucro:.2f}'

class ClienteApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AddClienteScreen(name='add'))
        sm.add_widget(ListClienteScreen(name='list'))
        sm.add_widget(DeleteClienteScreen(name='delete'))
        sm.add_widget(ProfitScreen(name='profit'))
        return sm

if __name__ == '__main__':
    ClienteApp().run()
