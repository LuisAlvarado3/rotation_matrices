from src.productPoint import ProductPoint
class MatrixProduct:
    def __init__(self, 
        matrix_a = ( (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), ), 
        matrix_b = ( (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), )
    ) -> None:
        self.matrix_a         = matrix_a
        self.matrix_b         = matrix_b
        self.resulting_matrix = list( )
        self.__calculate_matrix()

    def __calculate_matrix( self ) -> None:
        if len( self.matrix_a[0] ) == len( self.matrix_b ):
            matrix_auxiliar = self.__sort_matrix_B( )

            self.__multiply_matrices( matrix_auxiliar )


    def __sort_matrix_B( self ) -> list:
        matrix_auxiliar = []
        for column_b in range( len( self.matrix_b[0] ) ):

            vector_auxiliar = []
            for row_b in range( len( self.matrix_b ) ):
                vector_auxiliar.append(
                    self.matrix_b[ row_b ][ column_b ]
                )
            matrix_auxiliar.append( vector_auxiliar )
        
        return matrix_auxiliar

    def __multiply_matrices( self, matrix_b_inverted ) -> None:
        vertex_c  = []
        print("\n")
        for vertex_a in self.matrix_a:
            for vertex_b in matrix_b_inverted:
                obj_product_point = ProductPoint( 
                    vertex_a,
                    vertex_b
                )
                # print(obj_product_point.resulting)
                vertex_c.append( obj_product_point.resulting )
                # print( f"{vertex_a} X {vertex_b}")
            self.resulting_matrix.append( vertex_c )
            vertex_c = []



    def print_data( self ) -> None:
        for vector in self.resulting_matrix:
            print( vector )