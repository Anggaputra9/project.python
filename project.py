from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TicTacToeApp(App):
    def build(self):
        # Layout utama
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Label status untuk menampilkan giliran pemain atau pemenang
        self.status_label = Label(
            text="Player X's Turn",
            font_size=24,
            size_hint_y=0.2
        )
        self.root.add_widget(self.status_label)
        
        # Layout grid 3x3 untuk papan permainan
        self.grid = GridLayout(cols=3, spacing=5)
        self.root.add_widget(self.grid)
        
        # Inisialisasi papan permainan
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        # Tambahkan tombol-tombol ke grid
        for row in range(3):
            for col in range(3):
                button = Button(
                    text="",
                    font_size=32,
                    size_hint=(1, 1)
                )
                button.bind(on_press=lambda instance, x=row, y=col: self.make_move(instance, x, y))
                self.grid.add_widget(button)
                self.board[row][col] = button
        
        return self.root
    
    def make_move(self, button, row, col):
        # Periksa apakah kotak sudah diisi
        if button.text != "":
            return
        
        # Tandai kotak dengan simbol pemain saat ini
        button.text = self.current_player
        
        # Periksa apakah ada pemenang
        if self.check_winner():
            self.status_label.text = f"Player {self.current_player} Wins!"
            self.disable_board()
            return
        
        # Periksa apakah permainan seri
        if self.is_draw():
            self.status_label.text = "It's a Draw!"
            return
        
        # Ganti giliran pemain
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.text = f"Player {self.current_player}'s Turn"
    
    def check_winner(self):
        # Periksa baris, kolom, dan diagonal untuk pemenang
        for row in range(3):
            if self.board[row][0].text == self.board[row][1].text == self.board[row][2].text != "":
                return True
        for col in range(3):
            if self.board[0][col].text == self.board[1][col].text == self.board[2][col].text != "":
                return True
        if self.board[0][0].text == self.board[1][1].text == self.board[2][2].text != "":
            return True
        if self.board[0][2].text == self.board[1][1].text == self.board[2][0].text != "":
            return True
        return False
    
    def is_draw(self):
        # Periksa apakah semua kotak terisi
        for row in range(3):
            for col in range(3):
                if self.board[row][col].text == "":
                    return False
        return True
    
    def disable_board(self):
        # Nonaktifkan semua tombol di papan setelah permainan selesai
        for row in range(3):
            for col in range(3):
                self.board[row][col].disabled = True

# Jalankan aplikasi
if __name__ == '__main__':
    TicTacToeApp().run()
