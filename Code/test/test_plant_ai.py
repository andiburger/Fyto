import sys
sys.path.append("..")
from ai.plant_ai import identify_plant

def test_plant_ai():
    api_key = "2b10BguaUwxcFmzQXeSbveMb6O"
    # Test with a valid image path
    image_path = "test_images/Hortensie.jpg"  # Replace with a valid image path
    result = identify_plant(image_path,api_key=api_key)
    
    # Check if the result contains expected keys
    assert "name" in result
    assert "common_names" in result
    assert "confidence" in result

    print(result)
    # Check for error handling with an invalid image path
    invalid_image_path = "invalid_path.jpg"
    error_result = identify_plant(invalid_image_path,api_key=api_key)
    
    assert "error" in error_result

if __name__ == '__main__':
    test_plant_ai()