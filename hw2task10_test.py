import Task_10
from random import choice, randint
import unittest
from unittest.mock import patch
from io import StringIO

class TestMainFunction(unittest.TestCase):

  def test_input(self):
        input_value = [(-1.2198086282526373, 1.0072210610070034, False), (-2.362573924787358, 2.1219894758144204, False), (-2.9322299379764587, 5.531393700792739, True), (-0.21244266445224014, 4.163506680394899, False), (-1.993826853880341, 2.0360128511616065, False), (-2.6210266918203695, 5.319927950194274, True), (-0.49702076897927316, 1.8474783669919348, True), (-1.2895766464848055, 3.5301193078288127, False), (-1.4745369667676975, 4.025872853737827, False), (-2.1886022704337096, 4.856721082249294, False), (-0.5517483107788803, 4.127940743023919, False), (-2.6658942559219794, 4.926232368775843, True), (-0.20645790934928065, 4.679803636478647, False), (-0.9414267918877326, 5.47401140226449, False), (-1.76878067264903, 3.1273145825313757, False), (-0.03430630200565021, 3.988042493478848, False), (-1.8143912256012649, 1.6028957751088557, False), (-2.0243007417387124, 2.4535466915944197, False), (-1.5314134258910521, 1.8413274070041146, False), (-2.609642490880147, 4.633208559890351, True), (-0.31400096826420576, 0.9949201741142948, True), (-2.2209911182458573, 3.0630267881414452, False), (-1.0631299519507662, 0.1217165170846366, False), (-0.48159098769281083, 4.011035754517029, False), (-2.415272421122102, 5.637653302724481, True), (1.5716917408138449, -3.9585075125194984, False), (1.4469807706206013, 8.389397075268047, True), (1.1044713515795268, 5.193423683448465, True), (1.3408702617682382, 1.247645012704276, False), (1.5932449162925888, 3.5991198888567073, True), (0.4989661789093509, 2.379736837409671, False), (0.8352296131164585, 11.538836983465298, True), (1.4936886923663453, 6.603546340323349, True), (1.129245509498231, 7.329805032438996, True), (1.0539058435486257, 9.85065177871683, True), (1.4395057254758041, 6.566321510019604, True), (1.1576326208555556, 2.591895983023062, False), (0.3535108337025128, 11.956670226470356, True), (0.2660113423856585, 11.309101626179666, True), (0.17990559959862895, 2.4768672028945518, False), (1.6317113105274397, 3.786886979879089, True), (0.11778955535759428, 3.468016930015808, False), (0.34988653185757923, 6.114202937892248, True), (1.8545400066586208, 9.491055957811144, True), (0.26446956705846025, 8.814992735575006, True), (1.2970038895376002, 2.537047175054082, True), (1.4908668803318543, 4.263897410330629, True), (1.5074756361668935, 9.196917853861786, True), (0.8478360097808626, 7.223388740452184, True), (1.904152006957196, 11.450762597866344, True), (-0.6170355039354276, -1.6608763931739663, False), (0.039261055446843995, 0.40311171720846184, False), (-0.702994922686268, 0.9729802981996458, True), (0.7468751692795237, 0.7798178376296309, False), (0.995849150221227, 0.7097202626993118, True), (-0.8255934938400655, 0.468319753314278, False), (0.9876617333003204, 0.8508581852522566, True), (0.8199813972720797, 0.40760176558183525, True), (-0.34236794630303846, 0.3165704026184126, True), (-0.3789599991345227, 0.4135188527701479, True), (-0.8721049231987679, 0.6196914950147134, False), (0.2654126191958317, 0.9319343139212745, False), (-0.4323768112743811, 0.8253569208262115, True), (0.15692142626525918, 0.7868271725535284, False), (0.5191677083670336, 0.08983568504861217, True), (-0.7624865985812539, 0.9031300810425382, True), (-0.08644827344247852, 0.44957640883229677, True), (0.37360574109790456, 0.35380672026145776, False), (0.31072348835961283, 0.797313946749603, False), (-0.04478674941412475, 0.699917947572688, True), (0.06390058094485429, 0.7549397474935883, False), (0.4914883052964656, 0.28063069771628746, False), (-0.17299144513160347, 0.41303134114465756, True), (-0.8479214439688691, 0.7769751528769719, True), (-0.5410833943585818, 0.9442313562988599, True), (1.9686567843294083, -3.6276095784447056, False), (-0.5708185706772295, 0.014769999846306447, False), (0.26328023503299436, -1.6716981693490864, False), (1.3848378405247854, -4.726554667398929, False), (-1.0836900825498876, -2.2961179874546165, False), (-0.8871505987021204, -3.231764944324256, False), (1.049310031375704, 1.069176824504634, False), (-1.8355654538378579, -1.8252948625792458, False), (1.115716910928462, -3.453334667758002, False), (-1.357594901411276, -3.4485410287190468, False), (-1.513501093399864, -2.693964312631004, False), (-1.7754310626665344, -4.046611522942617, False), (-1.9240776775044757, -3.695986192271559, False), (1.2389622996695935, 1.3589034081877687, False), (-1.114862861003704, 0.4975244902667555, False), (1.024370517177434, -3.859640588021853, False), (-0.8990979379370168, -1.8654158356510329, False), (0.4719363007462216, -4.344540683779057, False), (-0.6986962993539767, -1.2655627297020549, False), (-0.39540531313230654, 1.0621249499754217, True), (-1.162540287627463, -4.051260351071704, False), (1.0523318764285148, -1.1205020243540647, False), (1.6037373387031453, -4.423988887219418, False), (0.2980121331406944, -1.2895201870309068, False), (-0.22545680890251862, 1.2587302481539018, True)]
        expected_output = ("The point is not in the shaded area", "The point is in the shaded area")
        
        for _ in range(randint(10,30)):
            test = choice(input_value)
            with patch('builtins.input', side_effect=test[:2]), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_10.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output[test[2]])

if __name__ == '__main__':
    unittest.main()
