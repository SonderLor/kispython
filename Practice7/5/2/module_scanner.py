import os
import graphviz


def scan_project(directory):
    ignore_dirs = [".idea", "__pycache__", "venv"]
    modules = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith(".py"):
                modules.append(os.path.join(root, file))
    return modules


def get_imports(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    imports = []
    for line in lines:
        if line.startswith("import"):
            imports.append(line.split()[1])
        elif line.startswith("from"):
            imports.append(line.split()[1])
    return imports


def draw_graph(directory):
    project_name = directory.split("\\")[-1]

    print(project_name)
    modules = scan_project(directory)

    graph = graphviz.Digraph()
    for module in modules:
        module_name = os.path.basename(module)
        graph.edge(project_name, module_name)
        imports = get_imports(module)
        for imp in imports:
            graph.edge(module_name, imp)

    graph.render("project_hierarchy", format="svg", cleanup=True)


if __name__ == "__main__":
    project_path = os.path.dirname(__file__)
    for i in range(2):
        project_path = os.path.dirname(project_path)
    draw_graph(project_path)
