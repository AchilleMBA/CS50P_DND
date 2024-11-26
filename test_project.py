import os
import pytest
from project import compare_texts
from unittest.mock import MagicMock, patch
from project import play_video


def test_process_audio_and_text():
    if not os.path.exists("greetingTemplate.txt"):
        pytest.fail("file is required for this test.")

def test_compare_texts():
    assert compare_texts("hello", "hello") is True
    # Mismatch in words
    assert compare_texts("hello", "hi") is False
    
    # Extra word
    assert compare_texts("hello", "hello my friend") is False
    
    # Missing word
    assert compare_texts("hello world", "") is False

def test_play_video():
    # Mock the OpenCV functions and objects
    mock_cap = MagicMock()
    mock_cap.isOpened.return_value = True
    mock_cap.read.side_effect = [(True, "frame1"), (True, "frame2"), (False, None)]  # Simulate frames and end of video
    
    with patch('cv2.VideoCapture', return_value=mock_cap) as mock_videocapture, \
         patch('cv2.imshow') as mock_imshow, \
         patch('cv2.waitKey', side_effect=[-1, -1, ord('q')]), \
         patch('cv2.destroyAllWindows') as mock_destroy:
        
        play_video("simulation_path")
        
        # Assertions to verify the behavior
        mock_videocapture.assert_called_once_with("simulation_path")
        assert mock_cap.isOpened.call_count == 1
        assert mock_cap.read.call_count == 3  # Two frames + end of video
        assert mock_imshow.call_count == 2  # Two frames displayed
        assert mock_destroy.call_count == 1  # Cleanup at the end



