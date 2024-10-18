# Class Button management



class Button :
    
    def __init__(self, image, position, text_input, background, color_background, color_text):

        self.image = image
        self.position_x = position[0]
        self.position_y = position[1]
        self.background = background
        self.color_background = color_background
        self.color_text = color_text
        self.text_input = text_input
        self.text = self.background.render(self.text_input, True, self.color_background)
        

        if (self.image is None) :

            self.image = self.text

        self.rect = self.image.get_rect(center = (self.position_x, self.position_y))
        self.text_rect = self.text.get_rect(center = (self.position_x, self.position_y))



    def update(self, window) :

        if (self.image is not None) :

            window.blit(self.image, self.rect)

        window.blit(self.text, self.text_rect)



    def checkPosition(self, position) :

        if (position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom)):

            return True

        return False



    def changeColor(self, position) :

        if (position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom)):

            self.text = self.background.render(self.text_input, True, self.color_text)

        else :
            
            self.text = self.background.render(self.text_input, True, self.color_background)