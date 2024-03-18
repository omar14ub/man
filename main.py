import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text="Click the button!", size_hint=(1, 0.5))
        layout.add_widget(self.label)
        
        button = Button(text="Click Me!", size_hint=(1, 0.5))
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)
        
        return layout
    
    def on_button_click(self, instance):
        self.label.text = "Button clicked!"
        
if __name__ == '__main__':
    SimpleApp().run()