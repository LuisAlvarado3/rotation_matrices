class ProductPoint:
    def __init__(self, vector1 = (0, 0, 0), vector2 = (0, 0, 0) ) -> None:
        self.resulting = 0
        self.vector1 = vector1
        self.vector2 = vector2
        self.calculate_vector()

    def calculate_vector( self ) -> None:
        if len( self.vector1 ) == len( self.vector2 ):
            for item in range( len( self.vector1) ):
                self.resulting += ( self.vector1[ item ] * self.vector2[ item ] )
            self.resulting = round( self.resulting, 4 )