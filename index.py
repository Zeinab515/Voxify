import flet as ft
from flet_audio import Audio
import requests
import os
from api_key import API_KEY
import time
from datetime import datetime

API_URL = "https://api.elevenlabs.io/v1/text-to-speech/"
VOICE_OPTIONS = {
    "Rachel (Female)": "21m00Tcm4TlvDq8ikWAM",
    "Bella (Female)": "EXAVITQu4vr4xnSDxMaL",
    "Domi (Female)": "AZnzlk1XvdUeBnXmlld",
    "Adam (Male)": "pNInz6obpgDQGcFmaJgB",
    "Antoni (Male)": "ErXwobaYiN019PkySvjV",
    "Josh (Male)": "TxGEqnHWrfWFTfGW9XjX",
}

SAVE_FOLDER = "GeneratedAudio"
os.makedirs(SAVE_FOLDER, exist_ok=True)


# HELPER FUNCTIONS

def generate_tts(text, voice_id):
    r = requests.post(
        API_URL + voice_id,
        headers={"xi-api-key": API_KEY},
        json={"text": text}
    )
    name = f"{time.time()}.mp3"
    path = os.path.join(SAVE_FOLDER, name)
    open(path, "wb").write(r.content)
    return path, name


# MAIN APPLICATION

def main(page: ft.Page):
    page.title = "AI Voice Generator"
    page.window_width = 980
    page.window_height = 720
    page.padding = 0
    page.bgcolor = "#070B14"
    
    history_list = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    
    def history_tile(item):
        return ft.Container(
            padding=ft.padding.all(14),
            border_radius=18,
            bgcolor="#0A1020",
            border=ft.border.all(1, "#16284A"),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        spacing=2,
                        expand=True,
                        controls=[
                            ft.Text(item["file"], size=13, weight=ft.FontWeight.W_600, color="#E5E7EB", no_wrap=True),
                            ft.Text(f'Voice: {item["voice"]} . {item["time"]}', size=11, color="#94A3B8"),
                        ],
                    ),
                ],
            ),
        )

    def add_to_history(name, path, voice):
        history_list.controls.insert(0,
            history_tile({
                "file": name,
                "path": path,
                "voice": voice,
                "time": datetime.now().strftime("%H:%M:%S")
            })
        )
        

    def clear_history(e):
        history_list.controls.clear()
        page.update()

    # File Import

    def on_file_picked(e):
        if e.files and len(e.files) > 0:
            file_path = e.files[0].path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    text_input.value = content
                    page.update()
            except Exception as ex:
                print(f"Error loading file: {str(ex)}")

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    # Inputs

    text_input = ft.TextField(
        label="Text",
        hint_text="Type or paste your text here…",
        multiline=True,
        min_lines=9,
        max_lines=13,
        text_size=14,
        border_radius=16,
        bgcolor="#0A1020",
        border_color="#1B2A4A",
        focused_border_color="#60A5FA",
        color="#E5E7EB",
        cursor_color="#60A5FA",
    )

    voice_dropdown = ft.Dropdown(
        label="Voice",
        value="Rachel (Female)",
        options=[ft.dropdown.Option(v) for v in VOICE_OPTIONS.keys()],
        width=320,
        border_radius=16,
        bgcolor="#0A1020",
        border_color="#1B2A4A",
        focused_border_color="#60A5FA",
        color="#E5E7EB",
    )
    
    #Actions

    def generate_voice(e):
        txt = (text_input.value or "").strip()
        if not txt:
            return
        
        voice_name = voice_dropdown.value
        voice_id = VOICE_OPTIONS[voice_name]
        result = generate_tts(txt, voice_id)
        if result[0] is None:
            return

        audio_path, file_name = result
        add_to_history(file_name, audio_path, voice_name)

        
        audio_player = Audio(src=audio_path, autoplay=True)
        page.overlay.append(audio_player)

        page.update()
    
    generate_button = ft.ElevatedButton(
        text="Generate",
        icon=ft.Icons.AUTO_AWESOME,
        on_click=generate_voice,
        style=ft.ButtonStyle(
            bgcolor="#2563EB",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=16),
            padding=ft.padding.symmetric(horizontal=18, vertical=14),
            elevation=2,
        ),
    )

    import_button = ft.IconButton(
        icon=ft.Icons.UPLOAD_FILE,
        icon_color="#60A5FA",
        tooltip="Import text file",
        on_click=lambda _: file_picker.pick_files(
            allowed_extensions=["txt"],
            dialog_title="Select a text file"
        ),
    )

    # Cards
    
    left_card = ft.Container(
        expand=True,
        padding=22,
        border_radius=24,
        bgcolor="#0B1220",
        border=ft.border.all(1, "#14213A"),
        content=ft.Column(
            spacing=14,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=2,
                            controls=[
                                ft.Text("Create audio", size=20, weight=ft.FontWeight.BOLD, color="#E5E7EB"),
                                ft.Text("Paste text, choose voice, generate & play", size=12, color="#94A3B8"),
                            ],
                        ),
                        import_button,
                    ],
                ),
                text_input,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[voice_dropdown, generate_button],
                ),
            ],
        ),
    )

    history_card = ft.Container(
        width=360,
        padding=22,
        border_radius=24,
        bgcolor="#0B1220",
        border=ft.border.all(1, "#14213A"),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=2,
                            controls=[
                                ft.Text("History", size=16, weight=ft.FontWeight.BOLD, color="#E5E7EB"),
                            ],
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color="#FCA5A5",
                            tooltip="Clear history",
                            on_click=clear_history,
                        ),
                    ],
                ),
                history_list,
            ],
        ),
    )
    
    content = ft.Container(
        expand=True,
        padding=ft.padding.all(22),
        content=ft.Row(expand=True, spacing=16, controls=[left_card, history_card]),
    )
    
    page.add(
        ft.Stack(
            expand=True,
            controls=[
                ft.Container(padding=ft.padding.only(left=40, top=30)),
                ft.Container(
                    padding=ft.padding.only(right=60, bottom=40),
                    alignment=ft.alignment.bottom_right,
                ),
                content,
            ],
        )
    )

ft.app(target=main)