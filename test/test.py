from speechcraft import text2voice, voice2voice, voice2embedding
from media_toolkit import AudioFile

sample_text = "I love society [laughs]! [happy] What a day to make voice overs with artificial intelligence."

# test text2speech
audio_numpy, sample_rate = text2voice(sample_text)
audio = AudioFile().from_np_array(audio_numpy, sr=sample_rate)
audio.save("en_speaker_3_i_love_socaity.wav")
#
## test voice cloning
embedding = voice2embedding(audio_file="test_files/voice_clone_test_voice_1.wav", voice_name="hermine").save_to_speaker_lib()
tts_new_speaker, sample_rate = text2voice(sample_text, voice="hermine")
audio_with_cloned_voice = AudioFile().from_np_array(tts_new_speaker, sr=sample_rate)
audio_with_cloned_voice.save("hermine_i_love_socaity.wav")

# test voice2voice
v2v_audio_np, sample_rate = voice2voice(audio_file="test_files/voice_clone_test_voice_2.wav", voice_name="hermine")
v2v_audio = AudioFile().from_np_array(v2v_audio_np, sr=sample_rate)
v2v_audio.save("potter_to_hermine.wav")
a = 1