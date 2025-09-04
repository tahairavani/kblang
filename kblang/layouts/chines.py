from .keyboard_layouts import KeyboardLayout


class ChLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._ch_layout = [
            '七', '我', '饿', '人', '他', '一', '鱼', '爱', '哦', '平', '【', '】', '、', 
            '啊', '是', '的', '发', '个', '和', '就', '看', '了', '；', '’', 
            '在', '小', '吃', '这', '不', '你', '吗', '，', '。', '／', '·', 
            '一', '二', '三', '四', '五', '六', '七', '八', '九', '零', '—', '＝'
        ]
        self._ch_shift_layout = [
            '七', '我', '饿', '人', '他', '一', '鱼', '爱', '哦', '平', '「', '」', '｜',
            '啊', '是', '的', '发', '个', '和', '就', '看', '了', '：', '“',
            '在', '小', '吃', '这', '不', '你', '吗', '，', '。', '？', '～',
            '！', '@', '#', '$', '%', '^', '&', '*', '（', '）', '——', '+'
        ]
        return [*self._ch_layout, *self._ch_shift_layout]
    
    @property
    def language_code(self) -> str:
        return "ch"