import dearpygui.dearpygui as dpg
from planning import *
import time, datetime

class MapNode:

    def __init__(self, x : int, y : int, state : str) -> None:
        self.x = x
        self.y = y
        self.state = state

    def __repr__(self) -> str:
        return "[{},{},{}]".format(self.x, self.y, self.state)

class GUI:

    def __init__(self) -> None:
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=600, height=600, resizable=True)
        dpg.setup_dearpygui()

        self.grid = [[MapNode(x,y,"AIR") for x in range(20)] for y in range(20)]

        self.time = -1

        self.colours = {
            0 : [255,0,0],
            1 : [0,255,0],
            2 : [0,0,255],
            3 : [0,0,0]
        }

        with dpg.window(label="PathFinder Window", width=dpg.get_viewport_max_width(), height=dpg.get_viewport_max_height()) as window:
            with dpg.handler_registry():
                dpg.add_mouse_down_handler(callback=self.select_cell)
                # basic usage of the table api
                self.initialize_grid(self.grid, window)

        dpg.show_viewport()

        self.paths = self.get_paths()

        start_time = time.time()

        # below replaces, start_dearpygui()
        while dpg.is_dearpygui_running():
            # insert here any code you would like to run in the render loop
            # you can manually stop by using stop_dearpygui()

            if not (abs(time.time() - start_time) <= 3):

                time_now = time.time()
                if abs(time_now - self.time) >= 0.2:
                    self.time = time_now

                    for i, path in enumerate(self.paths):
                        if len(path) != 0:
                            first = path.pop(0)
                            self.highlight((first.x, first.y), i)


            dpg.render_dearpygui_frame()

        dpg.destroy_context()

    def initialize_grid(self, grid, tag):

        min_x = 5
        min_y = 5
        self.window_size = 600

        self.cell_size = (self.window_size // 20) - 4
        colors = {
            "AIR" : [204, 185, 116]
        }

        self.node_grid = {}

        drawlist = dpg.add_drawlist(parent=tag, width=self.window_size, height=self.window_size, show=True)

        span = 0
        for row in grid:
            for node in row:
                nodeident = dpg.draw_rectangle([min_x+node.x*self.cell_size, min_y+node.y*self.cell_size], [min_x+(node.x+1)*self.cell_size, (node.y+1)*self.cell_size], color=colors[node.state], fill=colors[node.state], parent=drawlist)
                self.node_grid[(node.x, node.y)] = nodeident
            span += self.cell_size

        for col in range(20):
            # Collumns
            pass
            dpg.draw_rectangle([min_x+col*self.cell_size, 0], [min_x+(col+1)*self.cell_size, span], color=[0, 0, 0, 255], thickness=2, fill=[0, 0, 0, 0], parent=drawlist)

        dpg.draw_line([0, 0], [0, 520], color=[0, 0, 0], thickness=4, parent=drawlist)
        dpg.draw_line([0, 0], [525, 0], color=[0, 0, 0], thickness=4, parent=drawlist)
        dpg.draw_line([525, 520], [0, 520], color=[0, 0, 0], thickness=4, parent=drawlist)
        dpg.draw_line([525, 520], [525, 0], color=[0, 0, 0], thickness=4, parent=drawlist)  

        with dpg.handler_registry() as clickregistry:
            clickhandler = dpg.add_mouse_down_handler(callback=self.select_cell)

    def select_cell(self):

        pos = dpg.get_mouse_pos()

        try:
            node = self.node_grid[(pos[0] // self.cell_size, pos[1] // self.cell_size)]
        except KeyError:
            return

        dpg.configure_item(node, fill = [255,255,255])

    def highlight(self, position, colour):

        try:
            node = self.node_grid[position]
        except KeyError:
            return

        dpg.configure_item(node, fill = self.colours[colour])

    def get_paths(self):

        paths = []

        worldmap = Map(20, 20)

        for i in range(13):
            worldmap.setNodeBlocked(Node(i,i, None))

        for key in worldmap.nodes.keys():
            self.highlight(key, 3)

        manager = PathManager(worldmap)

        manager.addNode(5,6,9)
        manager.addNode(5,6,11)

        ## Getting Path 1
        paths.append(self.getPath(manager, Node(0,1,None), Node(14,6,None), 0))
        ## Getting Path 2
        paths.append(self.getPath(manager, Node(0,5,None), Node(20,20,None), 0))
        ## Getting path 3
        paths.append(self.getPath(manager, Node(0,5,None), Node(2,0,None), 0))

        return paths

    def getPath(self, manager : PathManager, node1 : Node, node2 : Node, time : int) -> Path:
        path = AStarPlanner(manager, node1, node2, time).findPath()
        for node in path.path:
            manager.addNode(node.x, node.y, path.path.index(node))
            
        return path.path


GUI()
