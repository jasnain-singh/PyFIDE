import pickle

_players_list = ['# Name Fed Rating +- B-Year',
                '1 Carlsen, Magnus\nNOR 2830   1990',
                '2 Caruana, Fabiano\nUSA 2803   1992',
                '3 Nakamura, Hikaru\nUSA 2789   1987',
                '4 Abdusattorov, Nodirbek\nUZB 2765   2004',
                '5 Ding, Liren\nCHN 2762   1992',
                '6 Firouzja, Alireza\nFRA 2760   2003',
                '7 Nepomniachtchi, Ian\nRUS 2758   1990',
                '8 So, Wesley\nUSA 2757   1993',
                '9 Erigaisi Arjun\nIND 2756   2003',
                '10 Wei, Yi\nCHN 2755   1999',
                '11 Anand, Viswanathan\nIND 2751   1969',
                '12 Karjakin, Sergey\nRUS 2750   1990',
                '13 Dominguez Perez, Leinier\nUSA 2748   1983',
                '14 Praggnanandhaa R\nIND 2747   2005',
                '15 Giri, Anish\nNED 2745   1994',
                '16 Gukesh D\nIND 2743   2006',
                '17 Mamedyarov, Shakhriyar\nAZE 2733   1985',
                '18 Maghsoodloo, Parham\nIRI 2732   2000',
                '19 Vachier-Lagrave, Maxime\nFRA 2732   1990',
                '20 Duda, Jan-Krzysztof\nPOL 2731   1998',
                '21 Le, Quang Liem\nVIE 2731   1991',
                '22 Aronian, Levon\nUSA 2729   1982',
                '23 Grischuk, Alexander\nRUS 2728   1983',
                '24 Yu, Yangyi\nCHN 2728   1994',
                '25 Vidit, Santosh Gujrathi\nIND 2727   1994',
                '26 Topalov, Veselin\nBUL 2727   1975',
                '27 Keymer, Vincent\nGER 2726   2004',
                '28 Radjabov, Teimour\nAZE 2723   1987',
                '29 Rapport, Richard\nROU 2719   1996',
                '30 Tabatabaei, M. Amin\nIRI 2707   2001',
                '31 Dubov, Daniil\nRUS 2707   1996',
                '32 Eljanov, Pavel\nUKR 2706   1983',
                '33 Artemiev, Vladislav\nRUS 2705   1998',
                '34 Esipenko, Andrey\nFID 2703   2002',
                '35 Sarana, Alexey\nSRB 2703   2000',
                '36 Wang, Hao\nCHN 2702   1989',
                '37 Harikrishna, Pentala\nIND 2701   1986',
                '38 Sevian, Samuel\nUSA 2698   2000',
                '39 Nihal Sarin\nIND 2698   2004',
                '40 Robson, Ray\nUSA 2695   1994',
                '41 Narayanan S L\nIND 2695   1998',
                '42 Deac, Bogdan-Daniel\nROU 2692   2001',
                '43 Fedoseev, Vladimir\nSLO 2690   1995',
                '44 Sjugirov, Sanan\nHUN 2689   1993',
                '45 Svidler, Peter\nFID 2689   1976',
                '46 Vitiugov, Nikita\nENG 2688   1987',
                '47 Bacrot, Etienne\nFRA 2686   1983',
                '48 Kasimdzhanov, Rustam\nUZB 2685   1979',
                '49 Bu, Xiangzhi\nCHN 2684   1985',
                '50 Sindarov, Javokhir\nUZB 2684   2005',
                '51 Tomashevsky, Evgeny\nRUS 2681   1987',
                '52 Navara, David\nCZE 2678   1985',
                '53 Amin, Bassem\nEGY 2678   1988',
                '54 Martirosyan, Haik M.\nARM 2678   2000',
                '55 Niemann, Hans Moke\nUSA 2676   2003',
                '56 Shevchenko, Kirill\nROU 2675   2002',
                '57 Howell, David W L\nENG 2675   1990',
                '58 Volokitin, Andrei\nUKR 2674   1986',
                '59 Predke, Alexandr\nSRB 2673   1994',
                '60 Adams, Michael\nENG 2673   1971',
                '61 Anton Guijarro, David\nESP 2673   1995',
                '62 Shankland, Sam\nUSA 2671   1991',
                '63 Sargissian, Gabriel\nARM 2671   1983',
                '64 Wojtaszek, Radoslaw\nPOL 2671   1987',
                '65 Oparin, Grigoriy\nUSA 2670   1997',
                '66 Saric, Ivan\nCRO 2670   1990',
                '67 Van Foreest, Jorden\nNED 2668   1999',
                '68 Leko, Peter\nHUN 2666   1979',
                '69 Yakubboev, Nodirbek\nUZB 2665   2002',
                '70 Grandelius, Nils\nSWE 2664   1993',
                '71 Najer, Evgeniy\nFID 2663   1977',
                '72 Aravindh, Chithambaram VR.\nIND 2662   1999',
                '73 Matlakov, Maxim\nRUS 2662   1991',
                '74 Gelfand, Boris\nISR 2661   1968',
                '75 Shirov, Alexei\nESP 2661   1972',
                '76 Naiditsch, Arkadij\nAZE 2661   1985',
                '77 Inarkiev, Ernesto\nFID 2658   1985',
                '78 Vallejo Pons, Francisco\nESP 2657   1982',
                '79 Alekseenko, Kirill\nAUT 2655   1997',
                '80 Kryvoruchko, Yuriy\nUKR 2654   1986',
                '81 Sadhwani, Raunak\nIND 2654   2005',
                '82 Wang, Yue\nCHN 2654   1987',
                '83 Korobov, Anton\nUKR 2651   1985',
                '84 Li, Chao b\nCHN 2651   1989',
                '85 Mamedov, Rauf\nAZE 2651   1988',
                '86 Bluebaum, Matthias\nGER 2649   1997',
                '87 Ni, Hua\nCHN 2649   1983',
                '88 Malakhov, Vladimir\nFID 2648   1980',
                '89 Bartel, Mateusz\nPOL 2647   1985',
                '90 Bjerre, Jonas Buhl\nDEN 2646   2004',
                '91 Ponomariov, Ruslan\nUKR 2646   1983',
                '92 Xiong, Jeffery\nUSA 2646   2000',
                '93 Ter-Sahakyan, Samvel\nARM 2644   1993',
                '94 Pichot, Alan\nESP 2644   1998',
                '95 Brkic, Ante\nCRO 2643   1988',
                '96 Nguyen, Thai Dai Van\nCZE 2643   2001',
                '97 Nabaty, Tamir\nISR 2643   1991',
                '98 Liang, Awonder\nUSA 2642   2003',
                '99 Ma, Qun\nCHN 2641   1991',
                '100 Yilmaz, Mustafa\nTUR 2641   1992']

with open('_players_list.pickle', 'wb') as f:
    pickle.dump(_players_list, f)