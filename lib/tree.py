class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    def depth_first_traversal(node):
        if node.get('id') == id:
          return node
          
        for child in node.get('children', []):
            result = depth_first_traversal(child)
            if result:
              return result
            
        return None

    if self.root:
      return depth_first_traversal(self.root)
    return None
