from multiprocessing import set_forkserver_preload
import tkinter as tk
cnt = 0
cnt_s = 0
cnt_w = 0
cnt_t = 0
cnt_c = 0
cnt_l = 0
centence = ["考えること","問題を解くこと","人と議論すること","勝つための作戦を考えること","数字や計算すること","勉強すること","興味ある領域を研究すること","分析すること","知ること","予想を当てること","最小の努力で最大の成果を狙う","戦略ゲームで遊ぶこと","誰も考えつかない新しいことを思いつく","友達や知り合いが増えること","人と会うこと","話すこと","話を聞くこと","SNSで多くの人と繋がること","人が集まるところに参加すること","人に人を紹介すること","噂話をしたり聴いたりすること","ファッションアイテムを見ることやオシャレを楽しむこと","何かを達成すること","高い目的を定めて挑戦すること","仕切ること","大きな変化を起こすこと","自分で決めること","人々を引っ張っていくこと","集団において責任ある役割を担うこと","自分なりの正義感に突き動かされて衝動的に行動すること","後輩などの世話を焼くこと","人に夢を語ること","人を勇気づけること"]
strength = []
weakness = []

f = open("./sw_result.txt","w")

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x200")
        self.question = tk.Label(self.root,
                                 text=centence[cnt])
        self.buttonS = tk.Button(self.root,
                                 text="強み",
                                 command=self.s_change)

        self.buttonW = tk.Button(self.root,
                                text="弱み",
                                command=self.w_change)
        self.s_result = tk.Label(self.root,
                                 text="")
        self.w_result = tk.Label(self.root,
                                 text="")
        
        self.question.pack()
        self.buttonS.pack(side=tk.LEFT)
        self.buttonW.pack(side=tk.RIGHT)
        self.s_result.pack()
        self.w_result.pack()
        self.root.mainloop()

    def changeText(self):
        if cnt >= len(centence):
            self.question['text'] = ""
            self.buttonS['text'] = ""
            self.buttonW['text'] = ""
            if len(strength) > 0:
                ans_s = "あなたの強みは"+str(cnt_s)+"個あります. "+"あなたの強みは, "+", ".join(strength)+"です."+"T: "+str(cnt_t)+"/13, C: "+str(cnt_c)+"/9, L: "+str(cnt_l)+"/11"
                self.s_result['text'] = ans_s
                f.write(ans_s+"\n")
            else:
                self.s_result['text'] = "あなたの強みはないです."
                f.write("あなたの強みはないです.\n")
            if len(weakness) > 0:
                ans_w = "あなたの弱みは"+str(cnt_w)+"個あります. "+"あなたの弱みは, "+", ".join(weakness)+"です."
                self.w_result['text'] = ans_w
                f.write(ans_w+"\n")
            else:
                self.w_result['text'] = "あなたの弱みはないです."
                f.write("あなたの弱みはないです.\n")
            #end = tk.Label(self.root, text="end!")
            #end.pack()
            f.close()
        else:
            self.question['text'] = centence[cnt]
    def tcl_check(self,num):
        global cnt_t
        global cnt_c
        global cnt_l
        if num < 13:
            cnt_t += 1
        elif 13 <= num < 22:
            cnt_c += 1
        else:
            cnt_l += 1
    def s_change(self):
        global cnt
        global cnt_s
        strength.append(centence[cnt])
        self.tcl_check(cnt)
        cnt += 1
        cnt_s += 1
        self.changeText()
    def w_change(self):
        global cnt
        global cnt_w
        weakness.append(centence[cnt])
        cnt += 1
        cnt_w += 1
        self.changeText()
    

app=Test()
