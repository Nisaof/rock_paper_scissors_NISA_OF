def tas_kagit_makas_NISA_OF():
    import time
    import random
    print("OYUNUMA HOŞGELDİNİZ!\nUYARI!!!\n Unutma,benimle yani bir bilgisayarla yarışıyorsun:)\nBilmiyorsanız açıklıyorum.\nTaş-Kağıt-Makas Nedir?:\n Basit bir el oyunu olup, hem eğlenceli hem de karar vermede yardımcı olabilen 2 kişi arasında oynanan bir oyun türüdür.")
    print("Nasıl Oynanır?:\n Her 2 oyuncu da(biri sen biri ben) taş-kağıt-makas üçlüsünden birini seçer.\n Taş,makası yener.\n Makas,kağıdı yener.\n Kağıt,taşı yener.\n2 galibiyet alan oyuncu kazanır!")
    print("Oyun sırasında oyundan ayrılmak isterseniz exit ile ayrılabilir,devam etmek isterseniz bir sonraki hamlenizi seçebilirsiniz.\n DİKKAT!!!\nEğer ben(bilgisayar) oynamak istemezsem oyun biter:)")
    
    secenekler = ["Taş", "Kağıt", "Makas"]
    evet_hayir = ["evet", "hayır", "Evet", "Hayır","evet","Evet"]#Evet oranını artırmak için.
    
    pc_galibiyet = 0
    oyuncu_galibiyet = 0
    Round_number=1
    
    

    mood = True

    while mood:
        try:
            pc = random.choice(evet_hayir)
            oyuncu_secenek = input("Oynamak ister misiniz? (Evet ya da Hayır): ")
        except Exception as e:
            print(f"Lütfen tekrar deneyin: {e}")
            continue  
        
        if pc in ["hayır", "Hayır"] or oyuncu_secenek in ["hayır", "Hayır"]:
            mood = False
            
            if pc in ["hayır", "Hayır"] and oyuncu_secenek in ["Evet", "evet"]:
                print("Ben oynamak istemiyorum, başka zaman oynarız. Görüşmek üzere!")
            elif pc in ["Evet", "evet"] and oyuncu_secenek in ["hayır", "Hayır"]:
                print("Oyundan ayrılıyorsun demek. Benden korktuğunu biliyordum ;)")
            elif pc in ["hayır", "Hayır"] and oyuncu_secenek in ["hayır", "Hayır"]:
                print("Oyundan ayrılıyorsun demek. Duygularımız karşılıklıymış, ben de oynamak istemiyordum zaten!")
            break
        
        else:
            if oyuncu_galibiyet == 2 or pc_galibiyet == 2:
                if oyuncu_galibiyet == 2:
                    print("Şanslısın, bu seferlik sen kazandın.\nRound:{Round_number}")
                else:
                    print("Şaşırtmayan bir sonuç, tabii ki de ben kazandım :)\nRound:{Round_number}")
                break

            print("Oyun başlıyor...\nİlk harfler büyük yazılır unutma ;)")
            pc_secenek = random.choice(secenekler)
            oyuncu = input("1 deyince taş-kağıt-makas! tercihinizi giriniz:")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            
            if oyuncu == pc_secenek:
                print(f"Sen: {oyuncu}\nBen: {pc_secenek}\nBerabere!\nRound:{Round_number}")
                print("####################")
                Round_number +=1
            elif (oyuncu == "Taş" and pc_secenek == "Kağıt") or (oyuncu == "Kağıt" and pc_secenek == "Makas") or (oyuncu == "Makas" and pc_secenek == "Taş"):
                pc_galibiyet += 1
                print(f"Sen: {oyuncu}\nBen: {pc_secenek}\nBEN KAZANDIM!!!\nRound:{Round_number}")
                Round_number +=1
                print("####################")
            elif (oyuncu == "Taş" and pc_secenek == "Makas") or (oyuncu == "Kağıt" and pc_secenek == "Taş") or (oyuncu == "Makas" and pc_secenek == "Kağıt"):
                oyuncu_galibiyet += 1
                print(f"Sen: {oyuncu}\nBen: {pc_secenek}\nSana avans verdim. Sen kazandın.\nRound:{Round_number}")
                Round_number +=1
                print("####################")
            
            print(f"SKOR:\nSEN: {oyuncu_galibiyet}\nBEN: {pc_galibiyet}\nRound:{Round_number-1}")

tas_kagit_makas_NISA_OF()
