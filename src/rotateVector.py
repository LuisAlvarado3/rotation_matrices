from src.rotationMatrix import RotationMatrix
from src.matrixProduct  import MatrixProduct

def get_rotate_vector( vector_x_y_z = [1,1,1] , angle_x_y_z=[0,0,0] , order_by_angle = ("ALFA", "BETA", "THETA") ) -> None:
    
    final_vector = vector_x_y_z
    if final_vector[0] != 0 or final_vector[1] != 0 or final_vector[2] != 0:
        obj_rotation_matrix = RotationMatrix(angle_x_y_z)
        for name in order_by_angle:
            #--------------------- X ---------------------#
            if angle_x_y_z[0] != 0 and name == "ALFA":
                final_vector = get_matrix_product( final_vector, obj_rotation_matrix.MATRIX[ name ] )
            
            #--------------------- Y ---------------------#
            if angle_x_y_z[1] != 0 and name == "BETA":
                final_vector = get_matrix_product( final_vector, obj_rotation_matrix.MATRIX[ name ] )
            
            #--------------------- Z ---------------------#
            if angle_x_y_z[2] != 0 and name == "THETA":
                final_vector = get_matrix_product( final_vector, obj_rotation_matrix.MATRIX[ name ] )

    return final_vector

def get_matrix_product( vector_x_y_z, matrix_rotation ) -> None:
        vector = (
            ( vector_x_y_z[0], ),
            ( vector_x_y_z[1], ),
            ( vector_x_y_z[2], )
        )
        obj_matrix_product = MatrixProduct( matrix_rotation, vector )
        matrix_resultant = obj_matrix_product.resulting_matrix

        return [
            matrix_resultant[0][0],
            matrix_resultant[1][0],
            matrix_resultant[2][0], 
        ]