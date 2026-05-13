import numpy as np
import urenderer

# Crie uma cena com três objetos, um filho do outro:
# Objeto0 -> Objeto1 -> Objeto2
#
# Configure as transformações para que todos os objetos sejam visíveis e renderize a cena
#
# Altere a transformação do objeto avô dos outros e renderize a cena.
# Observe como que os objetos filhos se movem juntos

if __name__ == "__main__":
    urenderer.utils.clear_workdir("03-grandchild")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="03-grandchild")

    # Crie a cena

    cube = urenderer.node.Node()

    cube.translation = np.array([0, 0, -5], np.float64)
    cube.rotation = np.array([45, 45, 45], np.float64)
    cube.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()

    runtime.scene.add_child(cube)

    pyramid_1 = urenderer.node.Node()

    pyramid_1.translation = np.array([2, -1, 1], np.float64)
    pyramid_1.rotation = np.array([45, 0, 0], np.float64)
    pyramid_1.render_data = urenderer.geometry.polygonal_ifs.get_ifs_pyramid()

    cube.add_child(pyramid_1)

    pyramid_2 = urenderer.node.Node()

    pyramid_2.translation = np.array([1, -2, -3], np.float64)
    pyramid_2.rotation = np.array([45, 0, 0], np.float64)
    pyramid_2.render_data = urenderer.geometry.polygonal_ifs.get_ifs_pyramid()

    pyramid_1.add_child(pyramid_2)

    '''
    pyramid_2 = urenderer.node.Node()

    pyramid_2.translation = np.array([-1, 0, -3], np.float64)
    pyramid_2.render_data = urenderer.geometry.polygonal_ifs.get_ifs_pyramid()

    pyramid_1.add_child(pyramid_2)
    '''

    runtime.iter(capture=True)

    # Rotacione o nó avô
    cube.rotation = np.array([45, 0, 0], np.float64)

    runtime.iter(capture=True)
