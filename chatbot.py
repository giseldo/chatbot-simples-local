import gradio as gr
from PIL import Image
import numpy as np

def create_mosaic(images):
    # Carregar as imagens
    loaded_images = [Image.open(image) for image in images]
    
    # Determinar o tamanho do mosaico
    widths, heights = zip(*(img.size for img in loaded_images))
    total_width = sum(widths)
    max_height = max(heights)
    
    # Criar uma nova imagem para o mosaico
    mosaic = Image.new('RGB', (total_width, max_height))
    
    # Colar as imagens no mosaico
    x_offset = 0
    for img in loaded_images:
        mosaic.paste(img, (x_offset, 0))
        x_offset += img.width
    
    return mosaic

iface = gr.Interface(
    fn=create_mosaic,
    inputs=gr.inputs.File(file_count="multiple", type="file"),
    outputs="image",
    title="Mosaico de Imagens",
    description="Carregue várias imagens para criar um mosaico."
)

if __name__ == "__main__":
    iface.launch()
