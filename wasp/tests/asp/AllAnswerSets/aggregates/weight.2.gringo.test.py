input = """
1 1 2 1 71 70
1 1 2 1 73 72
1 1 2 1 75 74
1 1 2 1 77 76
1 1 2 1 70 78
1 1 2 1 72 79
1 1 2 1 74 80
1 1 2 1 76 81
1 1 2 1 78 82
1 1 2 1 79 83
1 1 2 1 80 84
1 1 2 1 81 85
1 86 2 1 70 71
1 87 2 1 78 70
1 88 2 1 82 78
1 89 1 0 82
1 90 2 1 72 73
1 91 2 1 79 72
1 92 2 1 83 79
1 93 1 0 83
1 94 2 1 74 75
1 95 2 1 80 74
1 96 2 1 84 80
1 97 1 0 84
1 98 2 1 76 77
1 99 2 1 81 76
1 100 2 1 85 81
1 101 1 0 85
1 102 1 1 71
1 103 1 1 73
1 104 1 1 75
1 105 1 1 77
2 106 4 0 2 89 93 97 101
1 107 1 0 106
1 1 1 0 107
2 108 4 0 2 102 103 104 105
1 109 1 0 108
1 1 1 0 109
2 110 4 0 2 86 90 94 98
1 111 1 0 110
1 1 1 0 111
2 112 4 0 2 87 91 95 99
1 113 1 0 112
1 1 1 0 113
2 114 4 0 2 88 92 96 100
1 115 1 0 114
1 1 1 0 115
1 116 2 1 117 86
1 118 2 1 119 87
1 120 2 1 121 88
1 122 2 1 123 102
1 116 2 1 117 90
1 118 2 1 119 91
1 120 2 1 121 92
1 122 2 1 123 103
1 116 2 1 117 94
1 118 2 1 119 95
1 120 2 1 121 96
1 122 2 1 123 104
1 116 2 1 117 98
1 118 2 1 119 99
1 120 2 1 121 100
1 122 2 1 123 105
1 124 1 1 121
1 125 1 1 123
1 126 1 1 117
1 127 1 1 119
1 124 1 1 121
1 128 2 1 117 125
1 129 2 1 119 126
1 130 2 1 121 127
1 131 2 1 119 128
1 132 2 1 121 129
1 133 2 1 121 131
1 134 1 0 89
1 135 1 0 93
1 136 1 0 97
1 137 1 0 101
1 138 1 0 86
1 139 1 0 87
1 140 1 0 88
1 141 1 0 102
1 142 1 0 90
1 143 1 0 91
1 144 1 0 92
1 145 1 0 103
1 146 1 0 94
1 147 1 0 95
1 148 1 0 96
1 149 1 0 104
1 150 1 0 98
1 151 1 0 99
1 152 1 0 100
1 153 1 0 105
1 154 2 0 102 123
1 155 2 0 103 123
1 156 2 0 104 123
1 157 2 0 105 123
1 158 2 0 86 117
1 159 2 0 90 117
1 160 2 0 94 117
1 161 2 0 98 117
1 162 2 0 87 119
1 163 2 0 91 119
1 164 2 0 95 119
1 165 2 0 99 119
1 166 2 0 88 121
1 167 2 0 92 121
1 168 2 0 96 121
1 169 2 0 100 121
1 170 2 0 124 134
1 171 2 0 124 135
1 172 2 0 124 136
1 173 2 0 124 137
1 174 2 0 125 138
1 175 2 0 126 139
1 176 2 0 127 140
1 177 2 0 125 142
1 178 2 0 126 143
1 179 2 0 127 144
1 180 2 0 125 146
1 181 2 0 126 147
1 182 2 0 127 148
1 183 2 0 125 150
1 184 2 0 126 151
1 185 2 0 127 152
1 186 2 0 125 158
1 187 2 0 125 159
1 188 2 0 125 160
1 189 2 0 125 161
1 190 2 0 126 162
1 191 2 0 126 163
1 192 2 0 126 164
1 193 2 0 126 165
1 194 2 0 127 166
1 195 2 0 127 167
1 196 2 0 127 168
1 197 2 0 127 169
1 198 2 0 130 170
1 199 2 0 130 171
1 200 2 0 130 172
1 201 2 0 130 173
1 202 2 0 128 175
1 203 2 0 129 176
1 204 2 0 128 178
1 205 2 0 129 179
1 206 2 0 128 181
1 207 2 0 129 182
1 208 2 0 128 184
1 209 2 0 129 185
1 210 2 0 128 190
1 211 2 0 128 191
1 212 2 0 128 192
1 213 2 0 128 193
1 214 2 0 129 194
1 215 2 0 129 195
1 216 2 0 129 196
1 217 2 0 129 197
1 218 2 0 132 198
1 219 2 0 132 199
1 220 2 0 132 200
1 221 2 0 132 201
1 222 2 0 131 203
1 223 2 0 131 205
1 224 2 0 131 207
1 225 2 0 131 209
1 226 2 0 131 214
1 227 2 0 131 215
1 228 2 0 131 216
1 229 2 0 131 217
1 230 2 0 133 219
1 231 2 0 133 221
1 232 2 0 133 218
1 233 2 0 133 220
1 234 1 0 138
1 235 1 0 139
1 236 1 0 140
1 237 1 0 141
1 238 1 0 142
1 239 1 0 143
1 240 1 0 144
1 241 1 0 145
1 242 1 0 146
1 243 1 0 147
1 244 1 0 148
1 245 1 0 149
1 246 1 0 150
1 247 1 0 151
1 248 1 0 152
1 249 1 0 153
1 250 1 0 154
1 251 1 0 155
1 252 1 0 156
1 253 1 0 157
1 254 1 0 158
1 255 1 0 159
1 256 1 0 160
1 257 1 0 161
1 258 1 0 162
1 259 1 0 163
1 260 1 0 164
1 261 1 0 165
1 262 1 0 166
1 263 1 0 167
1 264 1 0 168
1 265 1 0 169
1 266 1 0 170
1 267 1 0 171
1 268 1 0 172
1 269 1 0 173
1 270 1 0 174
1 271 1 0 175
1 272 1 0 176
1 273 1 0 177
1 274 1 0 178
1 275 1 0 179
1 276 1 0 180
1 277 1 0 181
1 278 1 0 182
1 279 1 0 183
1 280 1 0 184
1 281 1 0 185
1 282 1 0 186
1 283 1 0 187
1 284 1 0 188
1 285 1 0 189
1 286 1 0 190
1 287 1 0 191
1 288 1 0 192
1 289 1 0 193
1 290 1 0 194
1 291 1 0 195
1 292 1 0 196
1 293 1 0 197
1 294 1 0 198
1 295 1 0 199
1 296 1 0 200
1 297 1 0 201
1 298 1 0 202
1 299 1 0 203
1 300 1 0 204
1 301 1 0 205
1 302 1 0 206
1 303 1 0 207
1 304 1 0 208
1 305 1 0 209
1 306 1 0 210
1 307 1 0 211
1 308 1 0 212
1 309 1 0 213
1 310 1 0 214
1 311 1 0 215
1 312 1 0 216
1 313 1 0 217
1 314 1 0 218
1 315 1 0 219
1 316 1 0 220
1 317 1 0 221
1 318 1 0 222
1 319 1 0 223
1 320 1 0 224
1 321 1 0 225
1 322 1 0 226
1 323 1 0 227
1 324 1 0 228
1 325 1 0 229
1 326 1 0 230
1 327 1 0 231
1 328 1 0 232
1 329 1 0 233
5 330 266 96 0 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 23 23 23 23 28 28 28 28 39 39 39 39 45 45 45 45 53 81 51 70 53 81 51 70 53 81 51 70 53 81 51 70 53 81 51 70 23 23 23 28 28 28 39 39 39 45 45 45 53 81 51 70 53 81 51 70 53 81 51 70 53 81 51 70 23 23 28 28 39 39 45 45 53 81 51 70 53 81 51 70 53 81 51 70 23 28 39 45 53 81 51 70 81 70 53 51
1 331 1 0 330
1 1 1 0 331
1 332 2 0 90 117
1 333 2 0 94 117
1 334 2 0 98 117
1 332 2 0 91 119
1 333 2 0 95 119
1 334 2 0 99 119
1 332 2 0 92 121
1 333 2 0 96 121
1 334 2 0 100 121
1 335 2 0 332 73
1 336 2 0 332 72
1 337 2 0 332 79
1 338 2 0 332 83
1 339 2 0 333 75
1 340 2 0 333 74
1 341 2 0 333 80
1 342 2 0 333 84
1 343 2 0 334 77
1 344 2 0 334 76
1 345 2 0 334 81
1 346 2 0 334 85
1 335 1 0 339
1 336 1 0 340
1 337 1 0 341
1 338 1 0 342
1 339 1 0 343
1 340 1 0 344
1 341 1 0 345
1 342 1 0 346
1 1 3 0 335 102 123
1 1 3 0 339 103 123
1 1 3 0 343 104 123
1 1 3 0 336 86 117
1 1 3 0 340 90 117
1 1 3 0 344 94 117
1 1 3 0 337 87 119
1 1 3 0 341 91 119
1 1 3 0 345 95 119
1 1 3 0 338 88 121
1 1 3 0 342 92 121
1 1 3 0 346 96 121
3 20 71 70 78 82 73 72 79 83 75 74 80 84 77 76 81 85 123 117 119 121 0 0
0
5 leafWeightCardinality(1,53,23)
6 leafWeightCardinality(2,81,28)
7 leafWeightCardinality(3,51,39)
8 leafWeightCardinality(4,70,45)
15 leafCost(1,red,53)
16 leafCost(2,red,81)
17 leafCost(3,red,51)
18 leafCost(4,red,70)
19 leafCost(1,blue,23)
20 leafCost(2,blue,28)
21 leafCost(3,blue,39)
22 leafCost(4,blue,45)
23 leafCost(1,green,76)
24 leafCost(2,green,109)
25 leafCost(3,green,90)
26 leafCost(4,green,115)
27 leafMin(1,23)
28 leafMin(2,28)
29 leafMin(3,39)
30 leafMin(4,45)
14 max_total_weight(265)
31 repeat(53,5)
32 repeat(81,3)
33 repeat(51,5)
34 repeat(70,3)
35 repeat(23,11)
36 repeat(28,9)
37 repeat(39,6)
38 repeat(45,5)
39 repeat(53,3)
40 repeat(81,2)
41 repeat(51,2)
42 repeat(70,2)
43 assign(53)
44 assign(81)
45 assign(51)
46 assign(70)
47 assign(23)
48 assign(28)
49 assign(39)
50 assign(45)
51 maxim(53,5)
52 maxim(81,3)
53 maxim(51,5)
54 maxim(70,3)
55 maxim(23,11)
56 maxim(28,9)
57 maxim(39,6)
58 maxim(45,5)
59 assigned
60 limit(11)
13 num(5)
61 coloredPos(4)
62 coloredPos(3)
63 coloredPos(2)
64 coloredPos(1)
65 location(0)
66 location(4)
67 location(3)
68 location(2)
69 location(1)
71 lt(1,4)
70 lt(1,3)
78 lt(1,2)
82 lt(1,1)
73 lt(2,4)
72 lt(2,3)
79 lt(2,2)
83 lt(2,1)
75 lt(3,4)
74 lt(3,3)
80 lt(3,2)
84 lt(3,1)
77 lt(4,4)
76 lt(4,3)
81 lt(4,2)
85 lt(4,1)
86 leafPos(1,3)
87 leafPos(1,2)
88 leafPos(1,1)
89 leafPos(1,0)
90 leafPos(2,3)
91 leafPos(2,2)
92 leafPos(2,1)
93 leafPos(2,0)
94 leafPos(3,3)
95 leafPos(3,2)
96 leafPos(3,1)
97 leafPos(3,0)
98 leafPos(4,3)
99 leafPos(4,2)
100 leafPos(4,1)
101 leafPos(4,0)
102 leafPos(1,4)
103 leafPos(2,4)
104 leafPos(3,4)
105 leafPos(4,4)
123 posColor(4,green)
117 posColor(3,green)
119 posColor(2,green)
121 posColor(1,green)
116 posColor(3,blue)
118 posColor(2,blue)
120 posColor(1,blue)
122 posColor(4,blue)
124 iterate(0,1)
125 iterate(3,1)
126 iterate(2,1)
127 iterate(1,1)
128 iterate(2,2)
129 iterate(1,2)
130 iterate(0,2)
131 iterate(1,3)
132 iterate(0,3)
133 iterate(0,4)
134 cost(0,53,0)
135 cost(0,81,0)
136 cost(0,51,0)
137 cost(0,70,0)
138 cost(3,23,0)
139 cost(2,23,0)
140 cost(1,23,0)
141 cost(4,23,0)
142 cost(3,28,0)
143 cost(2,28,0)
144 cost(1,28,0)
145 cost(4,28,0)
146 cost(3,39,0)
147 cost(2,39,0)
148 cost(1,39,0)
149 cost(4,39,0)
150 cost(3,45,0)
151 cost(2,45,0)
152 cost(1,45,0)
153 cost(4,45,0)
154 cost(4,53,0)
155 cost(4,81,0)
156 cost(4,51,0)
157 cost(4,70,0)
158 cost(3,53,0)
159 cost(3,81,0)
160 cost(3,51,0)
161 cost(3,70,0)
162 cost(2,53,0)
163 cost(2,81,0)
164 cost(2,51,0)
165 cost(2,70,0)
166 cost(1,53,0)
167 cost(1,81,0)
168 cost(1,51,0)
169 cost(1,70,0)
170 cost(0,53,1)
171 cost(0,81,1)
172 cost(0,51,1)
173 cost(0,70,1)
174 cost(3,23,1)
175 cost(2,23,1)
176 cost(1,23,1)
177 cost(3,28,1)
178 cost(2,28,1)
179 cost(1,28,1)
180 cost(3,39,1)
181 cost(2,39,1)
182 cost(1,39,1)
183 cost(3,45,1)
184 cost(2,45,1)
185 cost(1,45,1)
186 cost(3,53,1)
187 cost(3,81,1)
188 cost(3,51,1)
189 cost(3,70,1)
190 cost(2,53,1)
191 cost(2,81,1)
192 cost(2,51,1)
193 cost(2,70,1)
194 cost(1,53,1)
195 cost(1,81,1)
196 cost(1,51,1)
197 cost(1,70,1)
198 cost(0,53,2)
199 cost(0,81,2)
200 cost(0,51,2)
201 cost(0,70,2)
202 cost(2,23,2)
203 cost(1,23,2)
204 cost(2,28,2)
205 cost(1,28,2)
206 cost(2,39,2)
207 cost(1,39,2)
208 cost(2,45,2)
209 cost(1,45,2)
210 cost(2,53,2)
211 cost(2,81,2)
212 cost(2,51,2)
213 cost(2,70,2)
214 cost(1,53,2)
215 cost(1,81,2)
216 cost(1,51,2)
217 cost(1,70,2)
218 cost(0,53,3)
219 cost(0,81,3)
220 cost(0,51,3)
221 cost(0,70,3)
222 cost(1,23,3)
223 cost(1,28,3)
224 cost(1,39,3)
225 cost(1,45,3)
226 cost(1,53,3)
227 cost(1,81,3)
228 cost(1,51,3)
229 cost(1,70,3)
230 cost(0,81,4)
231 cost(0,70,4)
232 cost(0,53,4)
233 cost(0,51,4)
234 scost(23,3,0)
235 scost(23,2,0)
236 scost(23,1,0)
237 scost(23,4,0)
238 scost(28,3,0)
239 scost(28,2,0)
240 scost(28,1,0)
241 scost(28,4,0)
242 scost(39,3,0)
243 scost(39,2,0)
244 scost(39,1,0)
245 scost(39,4,0)
246 scost(45,3,0)
247 scost(45,2,0)
248 scost(45,1,0)
249 scost(45,4,0)
250 scost(53,4,0)
251 scost(81,4,0)
252 scost(51,4,0)
253 scost(70,4,0)
254 scost(53,3,0)
255 scost(81,3,0)
256 scost(51,3,0)
257 scost(70,3,0)
258 scost(53,2,0)
259 scost(81,2,0)
260 scost(51,2,0)
261 scost(70,2,0)
262 scost(53,1,0)
263 scost(81,1,0)
264 scost(51,1,0)
265 scost(70,1,0)
266 scost(53,0,1)
267 scost(81,0,1)
268 scost(51,0,1)
269 scost(70,0,1)
270 scost(23,3,1)
271 scost(23,2,1)
272 scost(23,1,1)
273 scost(28,3,1)
274 scost(28,2,1)
275 scost(28,1,1)
276 scost(39,3,1)
277 scost(39,2,1)
278 scost(39,1,1)
279 scost(45,3,1)
280 scost(45,2,1)
281 scost(45,1,1)
282 scost(53,3,1)
283 scost(81,3,1)
284 scost(51,3,1)
285 scost(70,3,1)
286 scost(53,2,1)
287 scost(81,2,1)
288 scost(51,2,1)
289 scost(70,2,1)
290 scost(53,1,1)
291 scost(81,1,1)
292 scost(51,1,1)
293 scost(70,1,1)
294 scost(53,0,2)
295 scost(81,0,2)
296 scost(51,0,2)
297 scost(70,0,2)
298 scost(23,2,2)
299 scost(23,1,2)
300 scost(28,2,2)
301 scost(28,1,2)
302 scost(39,2,2)
303 scost(39,1,2)
304 scost(45,2,2)
305 scost(45,1,2)
306 scost(53,2,2)
307 scost(81,2,2)
308 scost(51,2,2)
309 scost(70,2,2)
310 scost(53,1,2)
311 scost(81,1,2)
312 scost(51,1,2)
313 scost(70,1,2)
314 scost(53,0,3)
315 scost(81,0,3)
316 scost(51,0,3)
317 scost(70,0,3)
318 scost(23,1,3)
319 scost(28,1,3)
320 scost(39,1,3)
321 scost(45,1,3)
322 scost(53,1,3)
323 scost(81,1,3)
324 scost(51,1,3)
325 scost(70,1,3)
326 scost(81,0,4)
327 scost(70,0,4)
328 scost(53,0,4)
329 scost(51,0,4)
332 starting(2)
333 starting(3)
334 starting(4)
335 started(1,4)
336 started(1,3)
337 started(1,2)
338 started(1,1)
339 started(2,4)
340 started(2,3)
341 started(2,2)
342 started(2,1)
343 started(3,4)
344 started(3,3)
345 started(3,2)
346 started(3,1)
2 color(red)
3 color(blue)
4 color(green)
9 innerNode(1)
10 innerNode(2)
11 innerNode(3)
12 innerNode(4)
0
B+
0
B-
1
0
1
"""
output = """
{cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), cost(2,28,0), lt(1,3), cost(1,39,0), lt(1,2), cost(0,53,1), cost(2,81,0), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), leafPos(1,0), posColor(2,green), posColor(3,green), iterate(3,1), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(81,2,0), scost(28,2,0), starting(2), lt(3,3), leafPos(3,1), scost(39,1,0), scost(53,0,1)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), lt(3,1), cost(0,51,1), lt(1,2), cost(2,81,0), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), posColor(2,green), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(81,2,0), scost(28,2,0), starting(2), iterate(3,1), lt(3,3), posColor(3,green), leafPos(1,1), scost(23,1,0), leafPos(3,0), scost(51,0,1)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), lt(3,1), cost(1,53,0), lt(1,2), cost(2,81,0), lt(3,2), lt(3,4), lt(2,3), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(28,2,0), lt(3,3), posColor(2,green), scost(81,2,0), starting(2), iterate(3,1), posColor(3,green), posColor(1,green), scost(23,1,0), leafPos(3,0), leafPos(1,1), scost(53,1,0)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(4,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), lt(3,1), cost(1,53,0), cost(1,53,1), lt(1,2), cost(1,23,1), lt(3,2), lt(3,4), lt(2,3), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(28,2,0), lt(3,3), iterate(3,1), iterate(1,1), posColor(3,green), posColor(1,green), leafPos(3,0), scost(23,1,0), scost(23,1,1), leafPos(1,1), scost(53,1,0), scost(53,1,1)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(4,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(2,28,0), cost(3,23,0), lt(3,1), cost(3,53,1), cost(3,53,0), lt(3,2), lt(3,4), lt(2,3), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(28,2,0), lt(3,3), iterate(3,1), iterate(1,1), posColor(3,green), posColor(1,green), leafPos(3,0), leafPos(1,3), scost(53,3,0), scost(23,3,0), scost(53,3,1), scost(23,3,1)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), lt(3,1), cost(0,51,1), lt(1,2), cost(1,23,1), lt(3,2), lt(3,4), cost(0,51,2), lt(2,3), iterate(0,1), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(28,2,0), lt(3,3), iterate(3,1), iterate(1,1), posColor(3,green), iterate(0,2), leafPos(3,0), scost(51,0,1), scost(51,0,2), leafPos(1,1), scost(23,1,0), scost(23,1,1)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(2,28,0), cost(3,23,0), cost(2,28,2), lt(3,1), cost(2,28,1), lt(3,2), lt(3,4), lt(2,3), iterate(3,1), leafPos(4,4), scost(45,4,0), leafPos(2,2), scost(28,2,0), lt(3,3), iterate(2,1), iterate(2,2), iterate(1,1), iterate(1,2), scost(28,2,1), iterate(1,3), scost(28,2,2), leafPos(3,0), posColor(1,green), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(2,4), cost(2,28,0), lt(1,3), cost(2,28,2), lt(1,2), cost(2,28,1), lt(3,4), lt(2,3), iterate(3,1), posColor(1,green), scost(45,4,0), leafPos(4,4), scost(28,2,0), leafPos(2,2), leafPos(1,0), leafPos(3,3), scost(39,3,0), scost(39,3,1), iterate(1,1), iterate(2,1), iterate(2,2), iterate(1,2), scost(28,2,1), iterate(1,3), scost(28,2,2)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(2,4), cost(2,28,0), lt(1,3), lt(1,2), cost(3,51,1), cost(3,51,0), lt(3,4), lt(2,3), iterate(3,1), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), leafPos(3,3), scost(39,3,0), scost(39,3,1), posColor(1,green), leafPos(1,0), iterate(1,1), posColor(3,green), scost(51,3,0), starting(3), scost(51,3,1), started(2,4)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), cost(2,28,0), lt(1,3), cost(1,39,0), cost(0,53,2), cost(1,39,1), lt(1,2), cost(0,53,1), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), iterate(3,1), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), lt(3,3), iterate(1,1), posColor(3,green), leafPos(1,0), leafPos(3,1), scost(39,1,0), scost(39,1,1), iterate(0,2), scost(53,0,1), scost(53,0,2)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(1,4), lt(1,1), lt(2,4), cost(2,28,0), lt(1,3), cost(1,39,0), cost(1,39,1), lt(1,2), cost(1,51,1), lt(3,2), lt(3,4), cost(1,51,0), lt(2,3), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), iterate(3,1), lt(3,3), iterate(1,1), posColor(3,green), leafPos(1,0), posColor(1,green), leafPos(3,1), scost(39,1,0), scost(51,1,0), scost(39,1,1), starting(3), scost(51,1,1), started(2,4), started(2,3)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(3,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(3,23,0), cost(4,70,0), lt(3,1), cost(2,28,1), lt(3,2), lt(3,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), scost(70,4,0), lt(3,3), iterate(2,1), scost(28,2,1), iterate(1,1), iterate(1,2), posColor(1,green), leafPos(3,0), leafPos(1,3), scost(23,3,0)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), lt(1,4), lt(2,4), cost(2,28,0), cost(3,23,0), cost(4,70,0), lt(3,1), cost(3,53,0), lt(3,2), lt(3,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), scost(70,4,0), lt(3,3), posColor(3,green), posColor(1,green), iterate(1,1), leafPos(3,0), leafPos(1,3), scost(53,3,0), scost(23,3,0)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), started(1,4), lt(1,4), lt(1,1), cost(3,39,0), lt(2,4), cost(2,28,0), lt(1,3), cost(4,70,0), lt(1,2), cost(3,51,0), lt(3,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), scost(70,4,0), posColor(1,green), iterate(1,1), posColor(3,green), leafPos(3,3), scost(39,3,0), scost(51,3,0), starting(3), started(2,4), leafPos(1,0)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(3,blue), lt(1,4), lt(1,1), cost(3,39,0), lt(2,4), cost(2,28,0), lt(1,3), cost(4,70,0), lt(1,2), cost(2,28,1), lt(3,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(45,4,0), leafPos(4,4), scost(70,4,0), posColor(1,green), iterate(1,1), leafPos(3,3), scost(39,3,0), iterate(2,1), leafPos(1,0), scost(28,2,1), iterate(1,2)}
{posColor(2,blue), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), cost(4,51,0), cost(3,45,0), cost(1,23,2), lt(1,2), cost(2,28,1), cost(1,23,1), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), scost(28,2,0), leafPos(2,2), iterate(2,1), scost(28,2,1), iterate(1,1), iterate(1,2), iterate(0,2), iterate(0,3), leafPos(1,1), scost(23,1,0), scost(23,1,1), scost(23,1,2), leafPos(4,3), scost(45,3,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), posColor(3,blue), lt(1,4), lt(1,1), lt(2,4), cost(2,28,0), lt(1,3), cost(4,51,0), cost(3,45,0), lt(1,2), cost(2,28,1), lt(4,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), leafPos(1,0), leafPos(4,3), scost(45,3,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,23,0), posColor(3,blue), lt(2,4), cost(2,28,0), cost(4,53,0), cost(3,45,0), lt(3,1), cost(2,28,1), lt(3,2), lt(3,4), lt(4,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), leafPos(1,4), scost(23,4,0), scost(53,4,0), leafPos(4,3), scost(45,3,0), lt(3,3), leafPos(3,0)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(3,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(3,23,0), cost(4,51,0), lt(4,1), cost(2,28,1), lt(4,2), lt(4,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), lt(4,3), leafPos(4,0), leafPos(1,3), scost(23,3,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(3,blue), cost(3,39,0), lt(2,4), cost(2,28,0), cost(4,53,0), lt(4,1), cost(2,28,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), lt(4,3), leafPos(4,0), leafPos(1,4), scost(23,4,0), scost(53,4,0), leafPos(3,3), scost(39,3,0)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), cost(3,39,1), cost(3,39,0), lt(2,4), cost(2,28,0), cost(2,28,2), lt(4,1), cost(2,28,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), iterate(3,1), iterate(2,2), iterate(1,3), scost(28,2,2), lt(4,3), leafPos(4,0), leafPos(1,4), scost(23,4,0), leafPos(3,3), scost(39,3,0), scost(39,3,1)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(2,28,0), cost(3,23,0), cost(2,28,2), lt(4,1), cost(2,28,1), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), iterate(3,1), iterate(2,2), iterate(1,3), scost(28,2,2), lt(4,3), leafPos(4,0), leafPos(1,3), scost(23,3,0), leafPos(3,4), scost(23,3,1), scost(39,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), cost(3,45,1), lt(2,4), cost(2,28,0), cost(2,28,2), cost(3,45,0), lt(3,1), cost(2,28,1), lt(3,2), lt(3,4), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), iterate(1,1), iterate(1,2), iterate(3,1), iterate(2,2), iterate(1,3), scost(28,2,2), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(1,4), scost(23,4,0), lt(3,3), leafPos(3,0)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), lt(1,1), cost(3,45,1), lt(2,4), cost(2,28,0), lt(1,3), cost(2,28,2), cost(3,45,0), lt(1,2), cost(2,28,1), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), scost(28,2,1), iterate(2,1), posColor(1,green), leafPos(1,0), iterate(1,1), iterate(1,2), iterate(3,1), iterate(2,2), leafPos(4,3), iterate(1,3), scost(28,2,2), scost(45,3,0), leafPos(3,4), scost(45,3,1), scost(39,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), cost(3,39,1), cost(3,39,0), lt(2,4), cost(2,28,0), lt(4,1), cost(3,51,1), cost(3,51,0), lt(3,4), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), posColor(1,green), iterate(3,1), lt(4,3), leafPos(1,4), scost(23,4,0), leafPos(4,0), leafPos(3,3), scost(39,3,0), scost(51,3,0), starting(3), scost(39,3,1), scost(51,3,1), started(2,4)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(4,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(2,28,0), cost(3,23,0), lt(4,1), cost(3,53,1), cost(3,53,0), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), posColor(1,green), iterate(3,1), leafPos(1,3), lt(4,3), scost(53,3,0), scost(23,3,0), scost(53,3,1), scost(23,3,1), leafPos(4,0), leafPos(3,4), scost(39,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(4,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), cost(1,53,0), cost(1,53,1), lt(4,1), lt(1,2), cost(1,23,1), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), posColor(1,green), iterate(3,1), leafPos(1,1), scost(53,1,0), scost(23,1,0), scost(53,1,1), scost(23,1,1), lt(4,3), leafPos(4,0), leafPos(3,4), scost(39,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(2,4), cost(2,28,0), cost(1,39,0), cost(1,39,1), lt(4,1), cost(1,51,1), lt(3,2), lt(3,4), cost(1,51,0), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), posColor(1,green), iterate(3,1), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), scost(39,1,1), starting(3), scost(51,1,1), started(2,4), started(2,3), lt(4,3), leafPos(4,0), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), lt(1,4), lt(2,4), cost(2,28,0), cost(3,23,0), cost(4,51,0), lt(4,1), cost(3,53,0), lt(4,2), lt(4,4), lt(2,3), posColor(4,green), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), posColor(1,green), lt(4,3), leafPos(4,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(1,3), scost(53,3,0), scost(23,3,0)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), cost(2,28,0), lt(1,3), cost(1,45,0), cost(0,53,2), cost(1,45,1), lt(1,2), cost(0,53,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), iterate(0,2), lt(4,3), iterate(3,1), leafPos(1,0), scost(53,0,1), scost(53,0,2), leafPos(4,1), scost(45,1,0), scost(45,1,1), leafPos(3,4), scost(39,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,23,0), posColor(4,blue), posColor(1,blue), lt(2,4), cost(2,28,0), cost(1,45,0), lt(3,1), cost(1,45,1), cost(0,51,1), lt(3,2), lt(3,4), cost(0,51,2), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(1,1), iterate(0,2), lt(4,3), iterate(3,1), leafPos(1,4), scost(23,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), scost(51,0,2), leafPos(4,1), scost(45,1,0), scost(45,1,1)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), cost(0,70,2), lt(4,1), lt(1,2), cost(0,70,1), cost(1,23,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(1,1), scost(23,1,0), scost(23,1,1), lt(4,3), leafPos(4,0), scost(70,0,1), scost(70,0,2), leafPos(3,4), scost(39,4,0)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), lt(4,1), lt(1,2), cost(0,70,1), cost(2,81,0), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(3,1), posColor(2,green), scost(81,2,0), starting(2), lt(4,3), leafPos(1,1), scost(23,1,0), leafPos(4,0), scost(70,0,1), leafPos(3,4), scost(39,4,0)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), cost(2,28,0), lt(1,3), cost(1,45,0), lt(1,2), cost(0,53,1), cost(2,81,0), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(3,1), lt(4,3), posColor(2,green), scost(81,2,0), starting(2), leafPos(1,0), scost(53,0,1), leafPos(4,1), scost(45,1,0), leafPos(3,4), scost(39,4,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(2,4), cost(2,28,0), cost(1,45,0), lt(3,1), cost(0,51,1), cost(2,81,0), lt(3,2), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(3,1), posColor(2,green), scost(81,2,0), starting(2), lt(4,3), leafPos(1,4), scost(23,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), leafPos(4,1), scost(45,1,0)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(2,4), cost(2,28,0), cost(1,39,0), lt(4,1), cost(0,70,1), cost(2,81,0), lt(3,2), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(3,1), leafPos(3,1), lt(3,3), scost(39,1,0), posColor(2,green), scost(81,2,0), starting(2), lt(4,3), leafPos(4,0), scost(70,0,1), leafPos(1,4), scost(23,4,0)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), lt(1,4), lt(2,4), cost(2,28,0), cost(1,23,0), lt(1,3), cost(1,53,0), lt(4,1), lt(1,2), cost(2,81,0), lt(4,2), lt(4,4), lt(2,3), scost(28,2,0), leafPos(2,2), posColor(3,green), iterate(3,1), posColor(1,green), posColor(2,green), scost(81,2,0), starting(2), lt(4,3), leafPos(4,0), leafPos(3,4), scost(39,4,0), leafPos(1,1), scost(53,1,0), scost(23,1,0)}
{cost(0,70,0), started(1,4), posColor(1,blue), lt(1,4), cost(2,23,0), cost(3,39,0), lt(2,4), lt(1,3), cost(1,28,0), lt(2,2), lt(4,1), cost(0,70,1), cost(2,53,0), cost(3,51,0), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), posColor(2,green), posColor(3,green), scost(51,3,0), starting(3), started(2,4), leafPos(1,2), scost(53,2,0), scost(23,2,0), lt(4,3), leafPos(4,0), scost(70,0,1), leafPos(2,1), scost(28,1,0)}
{cost(0,81,0), cost(4,23,0), posColor(3,blue), posColor(1,blue), cost(3,39,0), lt(2,4), lt(2,1), cost(1,45,0), cost(4,53,0), lt(2,2), cost(0,81,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), posColor(2,green), iterate(2,1), leafPos(4,1), lt(4,3), scost(45,1,0), leafPos(1,4), scost(23,4,0), scost(53,4,0), leafPos(2,0), scost(81,0,1)}
{cost(0,53,0), cost(4,28,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,39,0), lt(1,3), cost(1,45,0), cost(4,81,0), lt(1,2), cost(0,53,1), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), iterate(2,1), posColor(2,green), leafPos(4,1), lt(4,3), scost(45,1,0), leafPos(1,0), scost(53,0,1), leafPos(2,4), scost(81,4,0), scost(28,4,0)}
{cost(0,53,0), cost(4,45,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,39,0), lt(2,4), lt(1,3), cost(1,28,0), cost(4,70,0), lt(2,2), lt(1,2), cost(0,53,1), lt(3,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), iterate(2,1), posColor(2,green), leafPos(1,0), scost(53,0,1), leafPos(4,4), scost(45,4,0), scost(70,4,0), leafPos(2,1), scost(28,1,0)}
{cost(0,70,0), cost(4,23,0), posColor(3,blue), posColor(1,blue), cost(3,39,0), lt(2,4), cost(1,28,0), cost(4,53,0), lt(2,2), lt(4,1), cost(0,70,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), iterate(2,1), posColor(2,green), lt(4,3), leafPos(1,4), scost(23,4,0), scost(53,4,0), leafPos(4,0), scost(70,0,1), leafPos(2,1), scost(28,1,0)}
{cost(0,70,0), cost(4,28,0), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,39,0), cost(1,23,0), lt(1,3), cost(4,81,0), lt(4,1), lt(1,2), cost(0,70,1), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), iterate(2,1), posColor(2,green), leafPos(1,1), scost(23,1,0), lt(4,3), leafPos(4,0), scost(70,0,1), leafPos(2,4), scost(81,4,0), scost(28,4,0)}
{cost(0,81,0), cost(4,45,0), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,39,0), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(4,70,0), lt(2,2), lt(1,2), cost(0,81,1), lt(3,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(3,3), scost(39,3,0), iterate(2,1), posColor(2,green), leafPos(1,1), scost(23,1,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), leafPos(2,0), scost(81,0,1)}
{cost(0,70,0), cost(4,28,0), posColor(3,blue), lt(1,4), cost(3,39,0), cost(1,23,0), lt(1,3), cost(4,81,0), cost(1,53,0), lt(4,1), lt(1,2), lt(3,4), lt(4,2), lt(4,4), posColor(4,green), leafPos(3,3), scost(39,3,0), posColor(1,green), posColor(2,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), lt(4,3), leafPos(4,0), leafPos(2,4), scost(81,4,0), scost(28,4,0), iterate(2,1)}
{cost(0,81,0), cost(4,45,0), posColor(3,blue), lt(1,4), cost(3,39,0), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(4,70,0), cost(1,53,0), lt(2,2), lt(1,2), lt(3,4), lt(2,3), posColor(4,green), posColor(1,green), scost(39,3,0), leafPos(3,3), posColor(2,green), iterate(2,1), leafPos(1,1), scost(53,1,0), scost(23,1,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), leafPos(2,0)}
{cost(0,53,0), cost(4,45,0), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), lt(1,1), cost(3,39,0), lt(2,4), lt(1,3), cost(1,28,0), cost(4,70,0), cost(1,81,0), lt(2,2), lt(1,2), lt(3,4), lt(2,3), posColor(4,green), posColor(1,green), scost(39,3,0), leafPos(3,3), posColor(2,green), iterate(2,1), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(1,0), leafPos(4,4), scost(45,4,0), scost(70,4,0)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), started(1,4), lt(1,4), cost(2,23,0), cost(3,39,0), lt(2,4), lt(2,1), lt(1,3), cost(4,70,0), lt(2,2), cost(3,51,0), lt(3,4), lt(2,3), posColor(4,green), scost(39,3,0), leafPos(3,3), posColor(1,green), leafPos(4,4), scost(45,4,0), scost(70,4,0), iterate(1,1), leafPos(2,0), leafPos(1,2), scost(23,2,0), posColor(3,green), scost(51,3,0), starting(3), started(2,4)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(3,blue), lt(1,4), cost(2,23,0), cost(3,39,0), lt(2,4), lt(2,1), lt(1,3), cost(4,70,0), cost(2,23,1), lt(2,2), lt(3,4), lt(2,3), posColor(4,green), scost(39,3,0), leafPos(3,3), posColor(1,green), iterate(1,1), leafPos(4,4), scost(45,4,0), scost(70,4,0), iterate(2,1), leafPos(2,0), iterate(1,2), leafPos(1,2), scost(23,2,0), scost(23,2,1)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(3,blue), lt(1,4), cost(2,23,0), cost(3,39,0), lt(1,3), cost(4,81,0), cost(2,23,1), lt(4,1), lt(3,4), lt(4,2), lt(4,4), posColor(4,green), scost(39,3,0), leafPos(3,3), posColor(1,green), iterate(1,1), lt(4,3), leafPos(1,2), scost(23,2,0), leafPos(4,0), leafPos(2,4), scost(81,4,0), scost(28,4,0), iterate(2,1), iterate(1,2), scost(23,2,1)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(3,blue), lt(1,4), lt(1,1), cost(3,39,0), lt(1,3), cost(2,45,0), cost(4,81,0), lt(1,2), cost(2,45,1), lt(3,4), lt(4,4), posColor(4,green), scost(39,3,0), leafPos(3,3), posColor(1,green), iterate(1,1), lt(4,3), iterate(2,1), iterate(1,2), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(1,0), leafPos(4,2), scost(45,2,0), scost(45,2,1)}
{posColor(2,blue), cost(0,81,0), cost(4,23,0), posColor(3,blue), cost(3,39,0), lt(2,4), lt(2,1), cost(2,45,0), cost(4,53,0), lt(2,2), cost(2,45,1), lt(3,4), lt(4,4), lt(2,3), posColor(4,green), scost(39,3,0), leafPos(3,3), posColor(1,green), iterate(1,1), lt(4,3), iterate(2,1), iterate(1,2), leafPos(2,0), leafPos(1,4), leafPos(4,2), scost(23,4,0), scost(53,4,0), scost(45,2,0), scost(45,2,1)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), cost(3,39,1), cost(3,39,0), lt(2,4), cost(1,28,0), cost(1,81,0), lt(2,2), lt(4,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), scost(39,3,0), leafPos(3,3), posColor(1,green), iterate(3,1), scost(39,3,1), posColor(2,green), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), iterate(2,1), iterate(2,2), lt(4,3), leafPos(4,0), leafPos(1,4), scost(23,4,0)}
{cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(2,4), lt(1,3), cost(1,28,0), cost(1,81,0), lt(2,2), lt(1,2), lt(3,4), lt(2,3), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), posColor(2,green), posColor(1,green), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(4,4), scost(45,4,0), leafPos(1,0), iterate(2,1), iterate(2,2)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), started(3,2), cost(3,39,1), started(3,4), cost(3,39,0), lt(2,4), lt(2,1), cost(1,45,0), started(3,3), lt(2,2), cost(1,70,0), lt(3,4), lt(4,2), lt(4,4), lt(2,3), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), posColor(2,green), posColor(1,green), iterate(2,1), iterate(2,2), lt(4,3), leafPos(2,0), leafPos(1,4), leafPos(4,1), scost(23,4,0), scost(45,1,0), scost(70,1,0), starting(4), started(2,4), started(2,3)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), lt(1,1), started(3,2), cost(3,39,1), started(3,4), cost(3,39,0), lt(1,3), cost(1,45,0), started(3,3), lt(1,2), cost(1,70,0), lt(3,4), lt(4,2), lt(4,4), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), posColor(2,green), posColor(1,green), lt(4,3), iterate(2,1), iterate(2,2), leafPos(2,4), scost(28,4,0), leafPos(1,0), leafPos(4,1), scost(45,1,0), scost(70,1,0), starting(4), started(2,4), started(2,3)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,39,1), cost(3,39,0), cost(1,23,0), lt(1,3), cost(1,53,0), lt(4,1), lt(1,2), lt(3,4), lt(4,2), lt(4,4), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), posColor(2,green), posColor(1,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), lt(4,3), leafPos(4,0), leafPos(2,4), scost(28,4,0), iterate(2,1), iterate(2,2)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,39,1), cost(3,39,0), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(1,53,0), lt(2,2), lt(1,2), lt(3,4), lt(2,3), iterate(3,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), posColor(1,green), posColor(2,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), leafPos(4,4), scost(45,4,0), leafPos(2,0), iterate(2,1), iterate(2,2)}
{posColor(2,blue), cost(0,81,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), cost(3,39,1), cost(3,39,0), lt(2,4), lt(2,1), cost(2,45,0), cost(2,45,2), lt(2,2), cost(2,45,1), lt(3,4), lt(4,4), lt(2,3), iterate(3,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), posColor(1,green), iterate(1,1), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), lt(4,3), leafPos(4,2), scost(45,2,0), scost(45,2,1), scost(45,2,2), leafPos(2,0), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(1,3), cost(2,45,0), cost(2,45,2), lt(1,2), cost(2,45,1), lt(3,4), lt(4,4), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), lt(4,3), leafPos(4,2), scost(45,2,0), leafPos(2,4), iterate(2,1), iterate(2,2), scost(28,4,0), iterate(1,2), scost(45,2,1), iterate(1,3), leafPos(1,0), scost(45,2,2)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(1,3), cost(2,45,0), lt(1,2), cost(3,51,1), cost(3,51,0), lt(3,4), lt(4,4), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), lt(4,3), scost(51,3,0), leafPos(4,2), scost(51,3,1), posColor(3,green), scost(45,2,0), starting(3), started(2,4), leafPos(2,4), scost(28,4,0), leafPos(1,0)}
{posColor(2,blue), cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), cost(3,39,1), cost(3,39,0), lt(2,4), lt(2,1), cost(2,45,0), lt(2,2), cost(3,51,1), cost(3,51,0), lt(3,4), lt(4,4), lt(2,3), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), lt(4,3), scost(51,3,0), leafPos(4,2), scost(51,3,1), posColor(3,green), leafPos(2,0), scost(45,2,0), starting(3), started(2,4), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), started(1,4), lt(1,4), cost(3,39,1), cost(2,23,0), cost(3,39,0), lt(1,3), lt(4,1), cost(3,51,1), cost(3,51,0), lt(3,4), lt(4,2), lt(4,4), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), lt(4,3), leafPos(1,2), scost(23,2,0), leafPos(4,0), leafPos(2,4), scost(28,4,0), scost(51,3,0), scost(51,3,1), posColor(3,green), starting(3), started(2,4)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,39,1), cost(2,23,0), cost(3,39,0), lt(1,3), cost(2,23,2), cost(2,23,1), lt(4,1), lt(3,4), lt(4,2), lt(4,4), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), lt(4,3), leafPos(1,2), scost(23,2,0), leafPos(4,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(23,2,1), iterate(1,3), leafPos(2,4), scost(23,2,2), scost(28,4,0)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,39,1), cost(2,23,0), cost(3,39,0), lt(2,4), lt(2,1), lt(1,3), cost(2,23,2), cost(2,23,1), lt(2,2), lt(3,4), lt(2,3), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), leafPos(4,4), scost(45,4,0), leafPos(2,0), leafPos(1,2), scost(23,2,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(23,2,1), iterate(1,3), scost(23,2,2)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(4,blue), started(1,4), lt(1,4), cost(3,39,1), cost(2,23,0), cost(3,39,0), lt(2,4), lt(2,1), lt(1,3), lt(2,2), cost(3,51,1), cost(3,51,0), lt(3,4), lt(2,3), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), iterate(1,1), posColor(1,green), leafPos(4,4), scost(51,3,0), scost(45,4,0), scost(51,3,1), posColor(3,green), leafPos(2,0), starting(3), started(2,4), leafPos(1,2), scost(23,2,0)}
{cost(0,53,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(2,4), lt(1,3), cost(1,28,0), lt(2,2), lt(1,2), cost(0,53,1), lt(3,4), lt(2,3), iterate(0,1), scost(39,3,0), leafPos(3,3), iterate(3,1), scost(39,3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0), leafPos(2,1), scost(28,1,0), leafPos(1,0), scost(53,0,1)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,39,1), cost(3,39,0), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), lt(2,2), lt(1,2), cost(0,81,1), lt(3,4), lt(2,3), iterate(0,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), iterate(3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0), leafPos(2,0), leafPos(1,1), scost(81,0,1), scost(23,1,0)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,39,1), cost(3,39,0), cost(1,23,0), lt(1,3), lt(4,1), lt(1,2), cost(0,70,1), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), iterate(3,1), posColor(2,green), lt(4,3), iterate(2,1), iterate(2,2), leafPos(1,1), scost(23,1,0), leafPos(4,0), scost(70,0,1), leafPos(2,4), scost(28,4,0)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,39,1), cost(3,39,0), lt(1,3), cost(1,45,0), lt(1,2), cost(0,53,1), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), iterate(3,1), posColor(2,green), lt(4,3), iterate(2,1), iterate(2,2), leafPos(4,1), scost(45,1,0), leafPos(2,4), scost(28,4,0), leafPos(1,0), scost(53,0,1)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), cost(3,39,1), cost(3,39,0), lt(2,4), lt(2,1), cost(1,45,0), lt(2,2), cost(0,81,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), iterate(3,1), posColor(2,green), lt(4,3), iterate(2,1), iterate(2,2), leafPos(2,0), scost(81,0,1), leafPos(4,1), leafPos(1,4), scost(45,1,0), scost(23,4,0)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), cost(3,39,1), cost(3,39,0), lt(2,4), cost(1,28,0), lt(2,2), lt(4,1), cost(0,70,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(39,3,0), leafPos(3,3), scost(39,3,1), iterate(3,1), posColor(2,green), lt(4,3), leafPos(2,1), iterate(2,1), iterate(2,2), scost(28,1,0), leafPos(4,0), scost(70,0,1), leafPos(1,4), scost(23,4,0)}
{cost(0,51,0), cost(4,45,0), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), lt(2,4), cost(3,23,0), cost(1,28,0), cost(4,70,0), lt(3,1), cost(1,81,0), lt(2,2), lt(3,2), lt(3,4), lt(2,3), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), leafPos(3,0), leafPos(1,3), scost(23,3,0), iterate(2,1)}
{cost(0,53,0), cost(4,39,0), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), lt(1,1), lt(2,4), lt(1,3), cost(1,28,0), cost(4,51,0), cost(3,45,0), cost(1,81,0), lt(2,2), lt(1,2), lt(4,4), lt(2,3), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(4,3), scost(45,3,0), leafPos(1,0), iterate(2,1), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{cost(0,70,0), cost(4,39,0), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), lt(2,4), cost(3,23,0), cost(1,28,0), cost(4,51,0), cost(1,81,0), lt(2,2), lt(4,1), lt(4,2), lt(4,4), lt(2,3), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), lt(4,3), iterate(2,1), leafPos(4,0), leafPos(1,3), scost(23,3,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{cost(0,70,0), cost(4,39,0), posColor(3,blue), lt(1,4), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), cost(4,51,0), cost(1,53,0), lt(4,1), lt(1,2), lt(4,2), lt(4,4), posColor(4,green), posColor(1,green), posColor(2,green), lt(4,3), iterate(2,1), leafPos(1,1), scost(53,1,0), scost(23,1,0), leafPos(4,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(2,3), scost(28,3,0)}
{cost(0,53,0), cost(4,45,0), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(1,39,0), cost(4,70,0), lt(1,2), lt(3,2), lt(3,4), cost(1,51,0), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,3), scost(28,3,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), iterate(2,1), leafPos(1,0), leafPos(3,1), scost(39,1,0), scost(51,1,0), starting(3), started(2,4), started(2,3)}
{cost(0,51,0), cost(4,45,0), posColor(3,blue), lt(1,4), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), cost(4,70,0), lt(3,1), cost(1,53,0), lt(1,2), lt(3,2), lt(3,4), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,3), scost(28,3,0), leafPos(1,1), scost(53,1,0), scost(23,1,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), leafPos(3,0), iterate(2,1)}
{cost(0,81,0), cost(4,39,0), posColor(3,blue), lt(1,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(4,51,0), cost(3,45,0), cost(1,53,0), lt(2,2), lt(1,2), lt(4,4), lt(2,3), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,0), leafPos(1,1), scost(53,1,0), scost(23,1,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(4,3), scost(45,3,0), iterate(2,1)}
{cost(0,81,0), cost(4,45,0), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(1,39,0), cost(4,70,0), lt(2,2), lt(3,2), lt(3,4), cost(1,51,0), lt(2,3), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,0), lt(3,3), leafPos(3,1), scost(39,1,0), scost(51,1,0), starting(3), started(2,4), started(2,3), leafPos(1,3), scost(23,3,0), iterate(2,1), leafPos(4,4), scost(45,4,0), scost(70,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(3,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(4,81,0), cost(3,45,0), lt(3,1), cost(1,53,0), lt(1,2), lt(3,2), lt(3,4), lt(4,4), posColor(4,green), posColor(1,green), posColor(2,green), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(3,0), lt(3,3), leafPos(4,3), scost(45,3,0), leafPos(1,1), iterate(2,1), scost(53,1,0), scost(23,1,0)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), posColor(3,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(2,1), lt(1,3), cost(4,51,0), cost(3,45,0), cost(2,23,1), lt(2,2), lt(4,4), lt(2,3), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(1,2), scost(23,2,0), leafPos(4,3), scost(45,3,0), iterate(2,1), iterate(1,2), scost(23,2,1), leafPos(2,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(3,blue), lt(1,4), cost(2,23,0), lt(1,3), cost(4,81,0), cost(3,45,0), lt(3,1), cost(2,23,1), lt(3,2), lt(3,4), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(1,2), scost(23,2,0), leafPos(4,3), scost(45,3,0), iterate(2,1), iterate(1,2), scost(23,2,1), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(3,0), lt(3,3)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), started(1,4), lt(1,4), cost(2,23,0), lt(2,4), cost(3,28,0), lt(1,3), cost(4,70,0), lt(3,1), cost(3,81,0), lt(3,2), lt(3,4), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(1,2), scost(23,2,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), leafPos(3,0), leafPos(2,3), scost(28,3,0), posColor(3,green), scost(81,3,0), starting(2)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(3,blue), lt(1,4), cost(2,23,0), lt(2,4), cost(3,28,0), lt(1,3), cost(4,70,0), lt(3,1), cost(2,23,1), lt(3,2), lt(3,4), posColor(4,green), posColor(1,green), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), iterate(1,1), leafPos(1,2), scost(23,2,0), leafPos(3,0), leafPos(2,3), iterate(2,1), scost(28,3,0), iterate(1,2), scost(23,2,1)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(3,blue), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(2,39,0), cost(4,70,0), lt(2,2), cost(2,39,1), lt(3,4), lt(2,3), posColor(4,green), posColor(1,green), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), iterate(1,1), iterate(2,1), iterate(1,2), leafPos(2,0), leafPos(3,2), scost(39,2,0), scost(39,2,1), leafPos(1,3), scost(23,3,0)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(3,blue), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(2,39,0), cost(4,70,0), lt(1,2), cost(2,39,1), lt(3,4), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), iterate(2,1), iterate(1,2), leafPos(2,3), scost(28,3,0), leafPos(1,0), leafPos(3,2), scost(39,2,0), scost(39,2,1)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), started(1,4), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(2,39,0), cost(4,70,0), cost(3,81,0), lt(1,2), lt(3,4), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(4,4), scost(45,4,0), scost(70,4,0), posColor(3,green), lt(3,3), leafPos(2,3), scost(28,3,0), scost(81,3,0), starting(2), leafPos(3,2), scost(39,2,0), leafPos(1,0)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(2,39,0), cost(4,70,0), lt(2,2), cost(3,53,0), lt(3,4), lt(2,3), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(4,4), scost(45,4,0), scost(70,4,0), posColor(3,green), leafPos(2,0), lt(3,3), leafPos(3,2), scost(39,2,0), leafPos(1,3), scost(23,3,0), scost(53,3,0)}
{posColor(2,blue), cost(0,81,0), cost(4,23,0), posColor(3,blue), lt(2,4), lt(2,1), cost(2,39,0), cost(4,53,0), cost(3,45,0), lt(2,2), cost(2,39,1), lt(3,4), lt(4,4), lt(2,3), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(4,3), scost(45,3,0), iterate(2,1), iterate(1,2), leafPos(2,0), leafPos(1,4), scost(23,4,0), scost(53,4,0), lt(3,3), leafPos(3,2), scost(39,2,0), scost(39,2,1)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(3,blue), lt(1,4), lt(1,1), lt(1,3), cost(2,39,0), cost(4,81,0), cost(3,45,0), lt(1,2), cost(2,39,1), lt(3,4), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), leafPos(2,4), leafPos(4,3), scost(81,4,0), scost(28,4,0), scost(45,3,0), lt(3,3), iterate(2,1), iterate(1,2), leafPos(1,0), leafPos(3,2), scost(39,2,0), scost(39,2,1)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(3,blue), lt(1,4), cost(3,23,0), cost(2,39,0), cost(4,81,0), lt(4,1), cost(2,39,1), lt(3,4), lt(4,2), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), lt(4,3), iterate(2,1), iterate(1,2), leafPos(2,4), scost(81,4,0), scost(28,4,0), lt(3,3), leafPos(3,2), scost(39,2,0), scost(39,2,1), leafPos(4,0), leafPos(1,3), scost(23,3,0)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(3,blue), lt(1,4), cost(3,23,0), cost(2,45,0), cost(4,81,0), lt(3,1), cost(2,45,1), lt(3,2), lt(3,4), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), lt(4,3), iterate(2,1), iterate(1,2), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(3,0), lt(3,3), leafPos(1,3), leafPos(4,2), scost(23,3,0), scost(45,2,0), scost(45,2,1)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), posColor(3,blue), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(4,51,0), cost(2,45,0), lt(2,2), cost(2,45,1), lt(4,4), lt(2,3), posColor(4,green), posColor(1,green), iterate(1,1), lt(4,3), iterate(2,1), iterate(1,2), leafPos(2,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(1,3), leafPos(4,2), scost(23,3,0), scost(45,2,0), scost(45,2,1)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(3,blue), lt(2,4), cost(3,28,0), cost(2,39,0), cost(4,53,0), lt(4,1), cost(2,39,1), lt(3,4), lt(4,2), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), lt(4,3), iterate(2,1), iterate(1,2), leafPos(2,3), scost(28,3,0), leafPos(3,2), lt(3,3), scost(39,2,0), scost(39,2,1), leafPos(4,0), leafPos(1,4), scost(23,4,0), scost(53,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,23,0), posColor(3,blue), lt(2,4), cost(3,28,0), cost(2,45,0), cost(4,53,0), lt(3,1), cost(2,45,1), lt(3,2), lt(3,4), lt(4,4), posColor(4,green), iterate(1,1), posColor(1,green), lt(4,3), iterate(2,1), leafPos(2,3), iterate(1,2), scost(28,3,0), lt(3,3), leafPos(3,0), leafPos(1,4), leafPos(4,2), scost(23,4,0), scost(53,4,0), scost(45,2,0), scost(45,2,1)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), posColor(3,blue), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(4,51,0), cost(2,45,0), lt(1,2), cost(2,45,1), lt(4,4), posColor(4,green), iterate(1,1), posColor(1,green), lt(4,3), iterate(2,1), leafPos(2,3), leafPos(3,4), iterate(1,2), scost(28,3,0), scost(51,4,0), scost(39,4,0), leafPos(1,0), leafPos(4,2), scost(45,2,0), scost(45,2,1)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), started(1,4), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(4,51,0), cost(2,45,0), cost(3,81,0), lt(1,2), lt(4,4), posColor(4,green), iterate(1,1), posColor(1,green), lt(4,3), posColor(3,green), leafPos(2,3), scost(28,3,0), scost(81,3,0), starting(2), leafPos(1,0), leafPos(4,2), scost(45,2,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(4,51,0), cost(2,45,0), lt(2,2), cost(3,53,0), lt(4,4), lt(2,3), posColor(4,green), iterate(1,1), posColor(1,green), lt(4,3), posColor(3,green), leafPos(2,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(1,3), leafPos(4,2), scost(23,3,0), scost(53,3,0), scost(45,2,0)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), lt(1,4), cost(3,23,0), cost(2,39,0), cost(4,81,0), lt(4,1), cost(3,53,0), lt(3,4), lt(4,2), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), lt(4,3), posColor(3,green), leafPos(2,4), scost(81,4,0), scost(28,4,0), lt(3,3), leafPos(3,2), scost(39,2,0), leafPos(4,0), leafPos(1,3), scost(23,3,0), scost(53,3,0)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), lt(1,4), cost(3,23,0), cost(2,45,0), cost(4,81,0), lt(3,1), cost(3,53,0), lt(3,2), lt(3,4), lt(4,4), posColor(4,green), iterate(1,1), posColor(1,green), lt(4,3), posColor(3,green), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(3,0), lt(3,3), leafPos(1,3), leafPos(4,2), scost(23,3,0), scost(53,3,0), scost(45,2,0)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), started(1,4), lt(1,4), cost(2,23,0), lt(2,4), cost(3,28,0), lt(1,3), cost(4,51,0), cost(3,81,0), lt(4,1), lt(4,2), lt(4,4), posColor(4,green), iterate(1,1), posColor(1,green), lt(4,3), leafPos(1,2), scost(23,2,0), leafPos(2,3), scost(28,3,0), leafPos(4,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), posColor(3,green), scost(81,3,0), starting(2)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(3,blue), lt(1,4), cost(2,23,0), lt(2,4), cost(3,28,0), lt(1,3), cost(4,51,0), cost(2,23,1), lt(4,1), lt(4,2), lt(4,4), posColor(4,green), posColor(1,green), iterate(1,1), lt(4,3), leafPos(1,2), scost(23,2,0), iterate(2,1), leafPos(4,0), iterate(1,2), scost(23,2,1), leafPos(2,3), scost(28,3,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,28,1), cost(2,23,0), lt(2,4), cost(3,28,0), lt(1,3), cost(2,23,2), lt(3,1), cost(2,23,1), lt(3,2), lt(3,4), posColor(1,green), iterate(1,1), iterate(3,1), leafPos(4,4), scost(45,4,0), lt(3,3), leafPos(3,0), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(1,2), scost(23,2,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(23,2,1), iterate(1,3), scost(23,2,2)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,45,1), cost(2,23,0), lt(2,4), lt(2,1), lt(1,3), cost(2,23,2), cost(3,45,0), cost(2,23,1), lt(2,2), lt(4,4), lt(2,3), posColor(1,green), iterate(1,1), iterate(3,1), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(2,0), leafPos(3,4), scost(39,4,0), leafPos(1,2), scost(23,2,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(23,2,1), iterate(1,3), scost(23,2,2)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,45,1), cost(2,23,0), lt(1,3), cost(2,23,2), cost(3,45,0), lt(3,1), cost(2,23,1), lt(3,2), lt(3,4), lt(4,4), posColor(1,green), iterate(1,1), iterate(3,1), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), leafPos(1,2), scost(23,2,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(23,2,1), iterate(1,3), scost(23,2,2)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,23,1), cost(3,23,0), cost(2,45,0), cost(2,45,2), lt(3,1), cost(2,45,1), lt(3,2), lt(3,4), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), leafPos(1,3), scost(23,3,0), leafPos(4,2), scost(23,3,1), scost(45,2,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(45,2,1), iterate(1,3), scost(45,2,2)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(4,blue), lt(1,4), cost(3,23,1), cost(3,23,0), cost(2,45,0), lt(3,1), cost(3,53,1), cost(3,53,0), lt(3,2), lt(3,4), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(2,4), scost(28,4,0), posColor(3,green), lt(3,3), leafPos(3,0), leafPos(1,3), scost(23,3,0), leafPos(4,2), scost(53,3,0), scost(23,3,1), scost(45,2,0), scost(53,3,1)}
{posColor(2,blue), cost(0,51,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), cost(3,28,1), lt(2,4), cost(3,28,0), cost(2,45,0), cost(2,45,2), lt(3,1), cost(2,45,1), lt(3,2), lt(3,4), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), lt(3,3), leafPos(3,0), leafPos(2,3), leafPos(4,2), scost(28,3,0), scost(45,2,0), scost(28,3,1), leafPos(1,4), scost(23,4,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(45,2,1), iterate(1,3), scost(45,2,2)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), lt(1,1), cost(3,28,1), lt(2,4), cost(3,28,0), lt(1,3), cost(2,45,0), cost(2,45,2), lt(1,2), cost(2,45,1), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(3,4), scost(39,4,0), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(1,0), leafPos(4,2), scost(45,2,0), scost(45,2,1), scost(45,2,2)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(2,45,0), cost(2,45,2), lt(2,2), cost(2,45,1), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(3,4), scost(39,4,0), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(2,0), leafPos(1,3), leafPos(4,2), scost(23,3,0), scost(45,2,0), scost(23,3,1), scost(45,2,1), scost(45,2,2)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,28,1), cost(2,23,0), lt(2,4), cost(3,28,0), lt(1,3), cost(2,23,2), cost(2,23,1), lt(4,1), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(3,4), scost(39,4,0), iterate(2,1), iterate(2,2), leafPos(1,2), iterate(1,2), iterate(1,3), scost(23,2,0), scost(23,2,1), leafPos(4,0), scost(23,2,2), leafPos(2,3), scost(28,3,0), scost(28,3,1)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), posColor(4,blue), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(2,45,0), lt(2,2), cost(3,53,1), cost(3,53,0), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(3,4), posColor(3,green), scost(39,4,0), leafPos(2,0), leafPos(1,3), leafPos(4,2), scost(23,3,0), scost(53,3,0), scost(45,2,0), scost(23,3,1), scost(53,3,1)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(1,4), cost(2,23,0), lt(1,3), cost(1,39,0), cost(1,39,1), lt(4,1), cost(1,51,1), lt(3,2), lt(3,4), cost(1,51,0), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), lt(4,3), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), scost(39,1,1), starting(3), scost(51,1,1), started(2,4), started(2,3), posColor(3,green), leafPos(2,4), scost(28,4,0), leafPos(1,2), scost(23,2,0), leafPos(4,0)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(1,4), lt(1,1), lt(1,3), cost(1,39,0), cost(2,45,0), cost(1,39,1), lt(1,2), cost(1,51,1), lt(3,2), lt(3,4), cost(1,51,0), lt(4,4), iterate(3,1), posColor(1,green), iterate(1,1), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), scost(39,1,1), starting(3), scost(51,1,1), started(2,4), started(2,3), posColor(3,green), lt(4,3), leafPos(2,4), scost(28,4,0), leafPos(1,0), leafPos(4,2), scost(45,2,0)}
{posColor(2,blue), cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(2,4), lt(2,1), cost(1,39,0), cost(2,45,0), cost(1,39,1), lt(2,2), cost(1,51,1), lt(3,2), lt(3,4), cost(1,51,0), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), iterate(1,1), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), scost(39,1,1), starting(3), scost(51,1,1), started(2,4), started(2,3), posColor(3,green), lt(4,3), leafPos(2,0), leafPos(4,2), scost(45,2,0), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(1,4), cost(2,23,0), lt(2,4), lt(2,1), lt(1,3), cost(1,39,0), cost(1,39,1), lt(2,2), cost(1,51,1), lt(3,2), lt(3,4), cost(1,51,0), lt(2,3), iterate(3,1), posColor(1,green), iterate(1,1), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), scost(39,1,1), starting(3), scost(51,1,1), started(2,4), started(2,3), posColor(3,green), leafPos(4,4), scost(45,4,0), leafPos(2,0), leafPos(1,2), scost(23,2,0)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), lt(1,1), cost(3,28,1), lt(2,4), cost(3,28,0), lt(1,3), cost(2,39,0), cost(2,39,2), lt(1,2), cost(2,39,1), lt(3,4), iterate(3,1), posColor(1,green), iterate(1,1), leafPos(3,2), lt(3,3), scost(39,2,0), iterate(2,1), iterate(2,2), iterate(1,2), scost(39,2,1), iterate(1,3), scost(39,2,2), leafPos(4,4), scost(45,4,0), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(1,0)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(2,39,0), cost(2,39,2), lt(2,2), cost(2,39,1), lt(3,4), lt(2,3), iterate(3,1), iterate(1,1), posColor(1,green), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(3,2), lt(3,3), scost(39,2,0), scost(39,2,1), scost(39,2,2), leafPos(4,4), scost(45,4,0), leafPos(2,0), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{posColor(2,blue), cost(0,81,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), cost(3,45,1), lt(2,4), lt(2,1), cost(2,39,0), cost(2,39,2), cost(3,45,0), lt(2,2), cost(2,39,1), lt(3,4), lt(4,4), lt(2,3), iterate(3,1), iterate(1,1), posColor(1,green), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(3,2), lt(3,3), scost(39,2,0), scost(39,2,1), scost(39,2,2), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(2,0), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), lt(1,1), cost(3,45,1), lt(1,3), cost(2,39,0), cost(2,39,2), cost(3,45,0), lt(1,2), cost(2,39,1), lt(3,4), lt(4,4), iterate(3,1), iterate(1,1), posColor(1,green), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(3,2), lt(3,3), scost(39,2,0), scost(39,2,1), scost(39,2,2), leafPos(2,4), leafPos(4,3), scost(28,4,0), scost(45,3,0), leafPos(1,0), scost(45,3,1)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,23,1), cost(3,23,0), cost(2,39,0), cost(2,39,2), lt(4,1), cost(2,39,1), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), iterate(1,1), posColor(1,green), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(3,2), lt(3,3), scost(39,2,0), lt(4,3), scost(39,2,1), scost(39,2,2), leafPos(4,0), leafPos(1,3), leafPos(2,4), scost(23,3,0), scost(28,4,0), scost(23,3,1)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), cost(3,28,1), lt(2,4), cost(3,28,0), cost(2,39,0), cost(2,39,2), lt(4,1), cost(2,39,1), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), iterate(1,1), posColor(1,green), iterate(2,1), iterate(2,2), iterate(1,2), iterate(1,3), leafPos(3,2), lt(3,3), scost(39,2,0), lt(4,3), scost(39,2,1), scost(39,2,2), leafPos(4,0), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), lt(1,4), cost(3,23,1), cost(3,23,0), cost(2,39,0), lt(4,1), cost(3,53,1), cost(3,53,0), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), iterate(1,1), posColor(1,green), posColor(3,green), leafPos(3,2), lt(3,3), scost(39,2,0), lt(4,3), leafPos(4,0), leafPos(1,3), leafPos(2,4), scost(23,3,0), scost(53,3,0), scost(28,4,0), scost(23,3,1), scost(53,3,1)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(4,blue), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(2,39,0), lt(2,2), cost(3,53,1), cost(3,53,0), lt(3,4), lt(2,3), iterate(1,1), posColor(1,green), iterate(3,1), leafPos(3,2), lt(3,3), scost(39,2,0), posColor(3,green), leafPos(4,4), scost(45,4,0), leafPos(2,0), leafPos(1,3), scost(23,3,0), scost(53,3,0), scost(23,3,1), scost(53,3,1)}
{posColor(2,blue), cost(0,81,0), cost(4,45,0), posColor(4,blue), lt(1,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(2,39,0), cost(1,53,0), cost(1,53,1), lt(2,2), lt(1,2), cost(1,23,1), lt(3,4), lt(2,3), iterate(1,1), iterate(3,1), posColor(1,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), scost(53,1,1), scost(23,1,1), leafPos(3,2), lt(3,3), scost(39,2,0), posColor(3,green), leafPos(4,4), scost(45,4,0), leafPos(2,0)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(2,39,0), cost(1,53,0), cost(1,53,1), lt(4,1), lt(1,2), cost(1,23,1), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), iterate(1,1), posColor(1,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), scost(53,1,1), scost(23,1,1), leafPos(3,2), lt(3,3), scost(39,2,0), posColor(3,green), lt(4,3), leafPos(4,0), leafPos(2,4), scost(28,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(4,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(2,45,0), lt(3,1), cost(1,53,0), cost(1,53,1), lt(1,2), cost(1,23,1), lt(3,2), lt(3,4), lt(4,4), iterate(3,1), iterate(1,1), posColor(1,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), lt(4,3), scost(53,1,1), scost(23,1,1), posColor(3,green), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), leafPos(4,2), scost(45,2,0)}
{posColor(2,blue), cost(0,81,0), cost(4,39,0), posColor(4,blue), lt(1,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(2,45,0), cost(1,53,0), cost(1,53,1), lt(2,2), lt(1,2), cost(1,23,1), lt(4,4), lt(2,3), iterate(3,1), iterate(1,1), posColor(1,green), leafPos(1,1), scost(53,1,0), scost(23,1,0), lt(4,3), scost(53,1,1), scost(23,1,1), posColor(3,green), leafPos(2,0), leafPos(4,2), scost(45,2,0), leafPos(3,4), scost(39,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(2,39,0), cost(0,70,2), lt(4,1), lt(1,2), cost(0,70,1), cost(1,23,1), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(1,1), scost(23,1,0), scost(23,1,1), posColor(3,green), leafPos(3,2), lt(3,3), scost(39,2,0), lt(4,3), leafPos(4,0), scost(70,0,1), scost(70,0,2), leafPos(2,4), scost(28,4,0)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(2,45,0), lt(3,1), cost(0,51,1), lt(1,2), cost(1,23,1), lt(3,2), lt(3,4), cost(0,51,2), lt(4,4), iterate(0,1), iterate(3,1), scost(23,1,0), leafPos(1,1), scost(23,1,1), iterate(1,1), iterate(0,2), posColor(3,green), lt(4,3), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), scost(51,0,2), leafPos(4,2), scost(45,2,0)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,45,1), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(3,45,0), lt(2,2), lt(1,2), cost(0,81,1), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(2,green), leafPos(4,3), scost(45,3,0), scost(45,3,1), iterate(2,1), iterate(2,2), leafPos(2,0), scost(81,0,1), leafPos(3,4), scost(39,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,45,1), cost(1,23,0), lt(1,3), cost(3,45,0), lt(3,1), cost(0,51,1), lt(1,2), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(2,green), leafPos(4,3), scost(45,3,0), scost(45,3,1), iterate(2,1), iterate(2,2), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), scost(51,0,1)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(2,39,0), lt(2,2), lt(1,2), cost(0,81,1), cost(2,51,0), lt(3,4), lt(2,3), iterate(0,1), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(2,green), leafPos(4,4), scost(45,4,0), leafPos(3,2), lt(3,3), scost(51,2,0), scost(39,2,0), starting(3), leafPos(2,0), started(2,4), started(2,3), scost(81,0,1), posColor(3,green)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(2,39,0), lt(4,1), lt(1,2), cost(0,70,1), cost(2,51,0), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(2,green), lt(4,3), leafPos(3,2), lt(3,3), scost(51,2,0), scost(39,2,0), starting(3), started(2,4), started(2,3), leafPos(4,0), scost(70,0,1), leafPos(2,4), scost(28,4,0), posColor(3,green)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), started(3,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(2,45,0), started(3,3), lt(2,2), lt(1,2), cost(0,81,1), cost(2,70,0), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(2,green), lt(4,3), posColor(3,green), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3), leafPos(2,0), scost(81,0,1), leafPos(3,4), scost(39,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), started(3,4), cost(1,23,0), lt(1,3), cost(2,45,0), lt(3,1), started(3,3), cost(0,51,1), lt(1,2), cost(2,70,0), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), scost(23,1,0), leafPos(1,1), iterate(3,1), posColor(2,green), lt(4,3), posColor(3,green), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), leafPos(2,4), started(2,4), started(2,3), scost(28,4,0), lt(3,3), leafPos(3,0), scost(51,0,1)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), lt(4,1), lt(1,2), cost(0,70,1), lt(4,2), lt(4,4), iterate(0,1), scost(23,1,0), leafPos(1,1), iterate(3,1), posColor(2,green), leafPos(2,3), scost(28,3,0), scost(28,3,1), lt(4,3), iterate(2,1), iterate(2,2), leafPos(4,0), scost(70,0,1), leafPos(3,4), scost(39,4,0)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), lt(3,1), cost(0,51,1), lt(1,2), lt(3,2), lt(3,4), iterate(0,1), scost(23,1,0), leafPos(1,1), iterate(3,1), leafPos(2,3), scost(28,3,0), posColor(2,green), scost(28,3,1), leafPos(4,4), scost(45,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), iterate(2,1), iterate(2,2)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), lt(3,1), cost(1,53,0), lt(1,2), lt(3,2), lt(3,4), scost(23,1,0), leafPos(1,1), iterate(3,1), posColor(1,green), scost(53,1,0), posColor(2,green), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(4,4), scost(45,4,0), lt(3,3), leafPos(3,0), iterate(2,1), iterate(2,2)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), cost(1,53,0), lt(4,1), lt(1,2), lt(4,2), lt(4,4), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), posColor(2,green), leafPos(2,3), scost(28,3,0), lt(4,3), scost(28,3,1), iterate(2,1), iterate(2,2), leafPos(4,0), leafPos(3,4), scost(39,4,0)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), lt(1,4), cost(1,23,0), lt(1,3), cost(2,39,0), cost(1,53,0), lt(4,1), lt(1,2), cost(2,51,0), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), posColor(2,green), posColor(3,green), lt(4,3), leafPos(3,2), lt(3,3), scost(51,2,0), scost(39,2,0), starting(3), started(2,4), started(2,3), leafPos(4,0), leafPos(2,4), scost(28,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), lt(1,4), started(3,4), cost(1,23,0), lt(1,3), cost(2,45,0), lt(3,1), cost(1,53,0), started(3,3), lt(1,2), cost(2,70,0), lt(3,2), lt(3,4), lt(4,4), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), posColor(2,green), posColor(3,green), lt(4,3), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), lt(1,4), started(3,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(2,45,0), cost(1,53,0), started(3,3), lt(2,2), lt(1,2), cost(2,70,0), lt(4,4), lt(2,3), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), posColor(2,green), posColor(3,green), lt(4,3), leafPos(4,2), leafPos(2,0), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3), leafPos(3,4), scost(39,4,0)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), lt(1,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(2,39,0), cost(1,53,0), lt(2,2), lt(1,2), cost(2,51,0), lt(3,4), lt(2,3), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), posColor(2,green), posColor(3,green), leafPos(3,2), lt(3,3), scost(51,2,0), scost(39,2,0), starting(3), started(2,4), started(2,3), leafPos(4,4), scost(45,4,0), leafPos(2,0)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,45,1), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(3,45,0), cost(1,53,0), lt(2,2), lt(1,2), lt(4,4), lt(2,3), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), iterate(2,1), iterate(2,2), posColor(2,green), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(2,0), leafPos(3,4), scost(39,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), lt(1,4), cost(3,45,1), cost(1,23,0), lt(1,3), cost(3,45,0), lt(3,1), cost(1,53,0), lt(1,2), lt(3,2), lt(3,4), lt(4,4), iterate(3,1), scost(23,1,0), leafPos(1,1), posColor(1,green), scost(53,1,0), iterate(2,1), iterate(2,2), posColor(2,green), leafPos(4,3), leafPos(2,4), scost(45,3,0), scost(28,4,0), scost(45,3,1), lt(3,3), leafPos(3,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), started(3,2), cost(3,23,1), started(3,4), cost(3,23,0), cost(1,45,0), lt(3,1), started(3,3), cost(1,70,0), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), lt(4,3), leafPos(4,1), scost(45,1,0), scost(70,1,0), starting(4), started(2,4), started(2,3), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), started(3,2), cost(3,23,1), started(3,4), lt(2,4), lt(2,1), cost(3,23,0), cost(1,45,0), started(3,3), lt(2,2), cost(1,70,0), lt(4,2), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), lt(4,3), leafPos(4,1), scost(45,1,0), scost(70,1,0), starting(4), leafPos(2,0), started(2,4), started(2,3), leafPos(3,4), scost(39,4,0), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(3,23,0), cost(1,28,0), cost(1,81,0), lt(2,2), lt(4,1), lt(4,2), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), lt(4,3), leafPos(4,0), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(3,4), scost(39,4,0), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), cost(3,23,1), cost(3,23,0), cost(1,39,0), lt(4,1), lt(3,2), lt(3,4), cost(1,51,0), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), lt(4,3), leafPos(4,0), leafPos(2,4), scost(28,4,0), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), starting(3), leafPos(1,3), started(2,4), started(2,3), scost(23,3,0), scost(23,3,1)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), lt(1,1), cost(3,45,1), lt(1,3), cost(1,39,0), cost(3,45,0), lt(1,2), lt(3,2), lt(3,4), cost(1,51,0), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), scost(51,1,0), starting(3), leafPos(1,0), started(2,4), started(2,3)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), lt(1,1), cost(3,45,1), lt(2,4), lt(1,3), cost(1,28,0), cost(3,45,0), cost(1,81,0), lt(2,2), lt(1,2), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(3,4), scost(39,4,0), leafPos(1,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), cost(3,45,1), lt(2,4), cost(1,28,0), cost(3,45,0), lt(3,1), cost(1,81,0), lt(2,2), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,3), scost(45,3,0), scost(45,3,1), lt(3,3), leafPos(2,1), leafPos(3,0), starting(2), scost(28,1,0), scost(81,1,0), leafPos(1,4), scost(23,4,0)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), cost(3,45,1), lt(2,4), lt(2,1), cost(1,39,0), cost(3,45,0), lt(2,2), lt(3,2), lt(3,4), cost(1,51,0), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,3), leafPos(3,1), scost(45,3,0), lt(3,3), scost(39,1,0), scost(51,1,0), scost(45,3,1), starting(3), leafPos(2,0), started(2,4), started(2,3), leafPos(1,4), scost(23,4,0)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(1,39,0), lt(2,2), lt(3,2), lt(3,4), cost(1,51,0), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), scost(51,1,0), starting(3), leafPos(2,0), started(2,4), started(2,3), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(3,23,0), cost(1,28,0), lt(3,1), cost(1,81,0), lt(2,2), lt(3,2), lt(3,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0), leafPos(2,1), lt(3,3), starting(2), scost(28,1,0), scost(81,1,0), leafPos(3,0), leafPos(1,3), scost(23,3,0), scost(23,3,1)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), started(3,4), lt(2,4), lt(2,1), cost(1,39,0), cost(2,45,0), started(3,3), lt(2,2), cost(2,70,0), lt(3,2), lt(3,4), cost(1,51,0), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), posColor(3,green), lt(4,3), leafPos(3,1), lt(3,3), scost(39,1,0), scost(51,1,0), starting(3), leafPos(2,0), started(2,4), started(2,3), leafPos(4,2), leafPos(1,4), scost(70,2,0), starting(4), scost(45,2,0), scost(23,4,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(3,4), lt(2,4), cost(1,28,0), cost(2,45,0), lt(3,1), cost(1,81,0), started(3,3), lt(2,2), cost(2,70,0), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), posColor(3,green), lt(4,3), lt(3,3), leafPos(3,0), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(1,4), leafPos(4,2), scost(23,4,0), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), lt(1,4), lt(1,1), started(3,4), lt(2,4), lt(1,3), cost(1,28,0), cost(2,45,0), cost(1,81,0), started(3,3), lt(2,2), lt(1,2), cost(2,70,0), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), posColor(3,green), lt(4,3), leafPos(3,4), scost(39,4,0), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(1,0), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), started(2,2), lt(1,4), lt(1,1), started(3,4), lt(1,3), cost(1,39,0), cost(2,45,0), started(3,3), lt(1,2), cost(2,70,0), lt(3,2), lt(3,4), cost(1,51,0), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), posColor(3,green), lt(4,3), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), scost(51,1,0), starting(3), started(2,4), started(2,3), leafPos(1,0), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0)}
{cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), lt(1,4), lt(1,1), lt(2,4), lt(1,3), cost(1,28,0), cost(2,39,0), cost(1,81,0), lt(2,2), lt(1,2), cost(2,51,0), lt(3,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), leafPos(3,2), lt(3,3), scost(51,2,0), scost(39,2,0), starting(3), started(2,4), started(2,3), posColor(3,green), leafPos(1,0), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(4,4), scost(45,4,0)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), lt(2,4), cost(1,28,0), cost(2,39,0), cost(1,81,0), lt(2,2), lt(4,1), cost(2,51,0), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(3,1), posColor(1,green), posColor(2,green), posColor(3,green), leafPos(3,2), lt(3,3), scost(51,2,0), scost(39,2,0), starting(3), started(2,4), started(2,3), lt(4,3), leafPos(4,0), leafPos(2,1), starting(2), scost(28,1,0), scost(81,1,0), leafPos(1,4), scost(23,4,0)}
{cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), lt(1,1), cost(3,28,1), lt(2,4), cost(3,28,0), lt(1,3), cost(1,39,0), lt(1,2), lt(3,2), lt(3,4), cost(1,51,0), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(4,4), scost(45,4,0), lt(3,3), leafPos(1,0), leafPos(3,1), scost(39,1,0), scost(51,1,0), starting(3), started(2,4), started(2,3)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), lt(1,4), lt(1,1), started(3,2), cost(3,28,1), started(3,4), lt(2,4), cost(3,28,0), lt(1,3), cost(1,45,0), started(3,3), lt(1,2), cost(1,70,0), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,3), scost(28,3,0), scost(28,3,1), lt(4,3), leafPos(4,1), scost(45,1,0), scost(70,1,0), starting(4), started(2,4), started(2,3), leafPos(3,4), scost(39,4,0), leafPos(1,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), started(3,2), cost(3,28,1), started(3,4), lt(2,4), cost(3,28,0), cost(1,45,0), lt(3,1), started(3,3), cost(1,70,0), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,3), lt(4,3), scost(28,3,0), scost(28,3,1), lt(3,3), leafPos(4,1), leafPos(3,0), scost(45,1,0), scost(70,1,0), starting(4), started(2,4), started(2,3), leafPos(1,4), scost(23,4,0)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), started(1,2), posColor(3,blue), started(2,2), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,39,0), lt(4,1), lt(3,2), lt(3,4), cost(1,51,0), lt(4,2), lt(4,4), iterate(3,1), posColor(1,green), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,3), lt(4,3), leafPos(3,1), scost(28,3,0), lt(3,3), scost(39,1,0), scost(51,1,0), scost(28,3,1), starting(3), leafPos(4,0), started(2,4), started(2,3), leafPos(1,4), scost(23,4,0)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(2,4), lt(2,1), cost(2,39,0), cost(1,45,0), lt(2,2), cost(0,81,1), cost(2,51,0), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), leafPos(3,2), lt(3,3), scost(39,2,0), posColor(3,green), lt(4,3), leafPos(2,0), scost(81,0,1), leafPos(4,1), scost(45,1,0), posColor(2,green), scost(51,2,0), starting(3), started(2,4), started(2,3), leafPos(1,4), scost(23,4,0)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(2,4), cost(1,28,0), cost(2,39,0), lt(2,2), lt(4,1), cost(0,70,1), cost(2,51,0), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(39,2,0), leafPos(3,2), lt(3,3), posColor(3,green), iterate(3,1), lt(4,3), leafPos(2,1), scost(28,1,0), leafPos(4,0), scost(70,0,1), posColor(2,green), scost(51,2,0), starting(3), started(2,4), started(2,3), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,70,0), cost(4,23,0), posColor(4,blue), posColor(1,blue), lt(2,4), cost(1,28,0), cost(2,39,0), cost(0,70,2), cost(1,28,1), lt(2,2), lt(4,1), cost(0,70,1), lt(3,4), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), scost(39,2,0), leafPos(3,2), lt(3,3), posColor(3,green), iterate(3,1), lt(4,3), leafPos(2,1), iterate(1,1), scost(28,1,0), iterate(0,2), scost(28,1,1), leafPos(4,0), scost(70,0,1), scost(70,0,2), leafPos(1,4), scost(23,4,0)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(1,3), cost(2,39,0), cost(1,45,0), cost(0,53,2), cost(1,45,1), lt(1,2), cost(0,53,1), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), scost(39,2,0), leafPos(3,2), lt(3,3), posColor(3,green), iterate(3,1), lt(4,3), leafPos(2,4), scost(28,4,0), iterate(1,1), iterate(0,2), leafPos(4,1), scost(45,1,0), scost(45,1,1), leafPos(1,0), scost(53,0,1), scost(53,0,2)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(1,1), lt(1,3), cost(2,39,0), cost(1,45,0), lt(1,2), cost(0,53,1), cost(2,51,0), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), scost(39,2,0), leafPos(3,2), lt(3,3), iterate(3,1), posColor(3,green), lt(4,3), leafPos(2,4), scost(28,4,0), posColor(2,green), scost(51,2,0), starting(3), started(2,4), started(2,3), leafPos(1,0), leafPos(4,1), scost(53,0,1), scost(45,1,0)}
{cost(0,53,0), cost(4,45,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), lt(1,3), cost(1,28,0), cost(2,39,0), lt(2,2), lt(1,2), cost(0,53,1), cost(2,51,0), lt(3,4), lt(2,3), iterate(0,1), scost(39,2,0), leafPos(3,2), lt(3,3), iterate(3,1), posColor(3,green), posColor(2,green), scost(51,2,0), starting(3), started(2,4), started(2,3), leafPos(1,0), scost(53,0,1), leafPos(2,1), scost(28,1,0), leafPos(4,4), scost(45,4,0)}
{posColor(2,blue), cost(0,53,0), cost(4,45,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), lt(1,3), cost(1,28,0), cost(2,39,0), cost(0,53,2), cost(1,28,1), lt(2,2), lt(1,2), cost(0,53,1), lt(3,4), lt(2,3), iterate(0,1), scost(39,2,0), leafPos(3,2), lt(3,3), iterate(3,1), posColor(3,green), iterate(1,1), iterate(0,2), leafPos(4,4), scost(45,4,0), leafPos(2,1), scost(28,1,0), scost(28,1,1), leafPos(1,0), scost(53,0,1), scost(53,0,2)}
{cost(0,81,0), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), lt(2,1), cost(1,23,0), lt(1,3), cost(4,51,0), cost(3,45,0), lt(2,2), lt(1,2), cost(0,81,1), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(2,0), scost(81,0,1), posColor(2,green), leafPos(4,3), scost(45,3,0), leafPos(1,1), scost(23,1,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), iterate(2,1)}
{cost(0,81,0), cost(4,23,0), posColor(3,blue), posColor(1,blue), lt(2,4), lt(2,1), cost(1,39,0), cost(4,53,0), cost(3,45,0), lt(2,2), cost(0,81,1), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(2,0), scost(81,0,1), posColor(2,green), leafPos(4,3), scost(45,3,0), leafPos(1,4), scost(23,4,0), scost(53,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), iterate(2,1)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(2,1), lt(1,3), cost(1,45,0), lt(2,2), cost(0,81,1), cost(2,53,0), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), leafPos(2,0), scost(81,0,1), posColor(2,green), iterate(3,1), lt(4,3), leafPos(1,2), scost(53,2,0), scost(23,2,0), leafPos(4,1), scost(45,1,0), leafPos(3,4), scost(39,4,0), posColor(3,green)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), started(3,4), lt(2,4), lt(2,1), cost(1,39,0), cost(2,45,0), started(3,3), lt(2,2), cost(0,81,1), cost(2,70,0), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(0,1), lt(4,3), iterate(3,1), leafPos(2,0), scost(81,0,1), posColor(2,green), leafPos(1,4), scost(23,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3), posColor(3,green)}
{posColor(2,blue), cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(1,3), cost(1,45,0), lt(3,1), cost(1,45,1), cost(0,51,1), lt(3,2), lt(3,4), cost(0,51,2), lt(4,2), lt(4,4), iterate(0,1), lt(4,3), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(4,1), scost(45,1,0), scost(45,1,1), leafPos(1,2), scost(23,2,0), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), scost(51,0,2), posColor(3,green)}
{posColor(2,blue), cost(0,53,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(1,3), cost(1,39,0), cost(2,45,0), cost(0,53,2), cost(1,39,1), lt(1,2), cost(0,53,1), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), lt(4,3), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(4,2), scost(45,2,0), leafPos(1,0), scost(53,0,1), scost(53,0,2), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), scost(39,1,1), posColor(3,green)}
{posColor(2,blue), cost(0,51,0), cost(4,23,0), posColor(4,blue), posColor(1,blue), lt(2,4), cost(1,28,0), cost(2,45,0), lt(3,1), cost(0,51,1), cost(1,28,1), lt(2,2), lt(3,2), lt(3,4), cost(0,51,2), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), lt(4,3), iterate(1,1), iterate(0,2), leafPos(2,1), scost(28,1,0), scost(28,1,1), leafPos(4,2), scost(45,2,0), leafPos(1,4), scost(23,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), scost(51,0,2), posColor(3,green)}
{posColor(2,blue), cost(0,53,0), cost(4,39,0), posColor(4,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), lt(1,3), cost(1,28,0), cost(2,45,0), cost(0,53,2), cost(1,28,1), lt(2,2), lt(1,2), cost(0,53,1), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(2,1), scost(28,1,0), scost(28,1,1), lt(4,3), leafPos(4,2), scost(45,2,0), leafPos(1,0), scost(53,0,1), leafPos(3,4), scost(53,0,2), scost(39,4,0), posColor(3,green)}
{posColor(2,blue), cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(1,3), cost(1,28,0), cost(0,70,2), cost(1,28,1), lt(2,2), lt(4,1), cost(0,70,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(2,1), scost(28,1,0), scost(28,1,1), lt(4,3), leafPos(4,0), scost(70,0,1), leafPos(1,2), scost(70,0,2), scost(23,2,0), leafPos(3,4), scost(39,4,0), posColor(3,green)}
{posColor(2,blue), cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(1,3), cost(1,28,0), lt(3,1), cost(0,51,1), cost(1,28,1), lt(2,2), lt(3,2), lt(3,4), cost(0,51,2), lt(2,3), iterate(0,1), iterate(3,1), iterate(1,1), iterate(0,2), leafPos(2,1), scost(28,1,0), scost(28,1,1), posColor(3,green), leafPos(4,4), scost(45,4,0), lt(3,3), leafPos(3,0), scost(51,0,1), scost(51,0,2), leafPos(1,2), scost(23,2,0)}
{cost(0,81,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), cost(3,45,1), lt(2,4), lt(2,1), cost(1,39,0), cost(3,45,0), lt(2,2), cost(0,81,1), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,0), scost(81,0,1), leafPos(1,4), scost(23,4,0), leafPos(4,3), lt(3,3), scost(45,3,0), leafPos(3,1), scost(45,3,1), scost(39,1,0)}
{cost(0,53,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,28,1), lt(2,4), cost(3,28,0), lt(1,3), cost(1,39,0), lt(1,2), cost(0,53,1), lt(3,2), lt(3,4), iterate(0,1), iterate(3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0), leafPos(2,3), lt(3,3), scost(28,3,0), leafPos(3,1), scost(28,3,1), scost(39,1,0), leafPos(1,0), scost(53,0,1)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,45,1), lt(1,3), cost(1,39,0), cost(3,45,0), lt(1,2), cost(0,53,1), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), iterate(3,1), posColor(2,green), iterate(2,1), iterate(2,2), scost(45,3,0), leafPos(4,3), scost(45,3,1), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(1,0), scost(53,0,1)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,45,1), lt(2,4), lt(1,3), cost(1,28,0), cost(3,45,0), lt(2,2), lt(1,2), cost(0,53,1), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,1), scost(28,1,0), leafPos(3,4), scost(39,4,0), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(1,0), scost(53,0,1)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(2,1), lt(1,3), cost(1,39,0), lt(2,2), cost(0,81,1), cost(2,53,0), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), iterate(3,1), posColor(2,green), leafPos(2,0), scost(81,0,1), posColor(3,green), leafPos(4,4), scost(45,4,0), leafPos(3,1), lt(3,3), scost(39,1,0), leafPos(1,2), scost(53,2,0), scost(23,2,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,45,0), lt(3,1), cost(0,51,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), lt(4,3), posColor(2,green), scost(51,0,1), leafPos(3,0), lt(3,3), iterate(2,1), iterate(2,2), leafPos(4,1), scost(45,1,0), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(1,4), scost(23,4,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), cost(3,45,1), lt(2,4), cost(1,28,0), cost(3,45,0), lt(3,1), cost(0,51,1), lt(2,2), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), scost(51,0,1), leafPos(3,0), lt(3,3), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,1), scost(28,1,0), leafPos(4,3), scost(45,3,0), scost(45,3,1), leafPos(1,4), scost(23,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(1,3), cost(1,45,0), lt(3,1), cost(0,51,1), cost(2,53,0), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), posColor(2,green), scost(51,0,1), leafPos(3,0), posColor(3,green), lt(3,3), lt(4,3), leafPos(4,1), leafPos(1,2), scost(45,1,0), scost(23,2,0), scost(53,2,0), leafPos(2,4), scost(28,4,0)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(1,3), cost(1,28,0), lt(3,1), cost(0,51,1), lt(2,2), cost(2,53,0), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), iterate(3,1), scost(51,0,1), leafPos(3,0), lt(3,3), leafPos(2,1), posColor(3,green), posColor(2,green), scost(28,1,0), scost(23,2,0), leafPos(1,2), scost(53,2,0), leafPos(4,4), scost(45,4,0)}
{cost(0,51,0), cost(4,23,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), started(3,4), lt(2,4), cost(1,28,0), cost(2,45,0), lt(3,1), started(3,3), cost(0,51,1), lt(2,2), cost(2,70,0), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), scost(51,0,1), leafPos(3,0), lt(3,3), leafPos(2,1), posColor(3,green), posColor(2,green), scost(28,1,0), leafPos(1,4), scost(23,4,0), lt(4,3), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3)}
{cost(0,51,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(3,23,0), cost(1,28,0), lt(3,1), cost(0,51,1), lt(2,2), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), iterate(3,1), scost(51,0,1), leafPos(3,0), leafPos(1,3), lt(3,3), scost(23,3,0), scost(23,3,1), posColor(2,green), leafPos(2,1), scost(28,1,0), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,1), cost(3,23,0), cost(1,45,0), lt(3,1), cost(0,51,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), scost(51,0,1), leafPos(3,0), leafPos(1,3), lt(3,3), scost(23,3,0), leafPos(2,4), scost(23,3,1), scost(28,4,0), lt(4,3), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,1), scost(45,1,0)}
{cost(0,81,0), cost(4,45,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(1,39,0), lt(2,2), cost(0,81,1), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), iterate(3,1), leafPos(1,3), scost(23,3,0), scost(23,3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(4,4), scost(45,4,0), leafPos(3,1), lt(3,3), scost(39,1,0), leafPos(2,0), scost(81,0,1)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,1), lt(2,4), cost(3,23,0), cost(1,28,0), lt(2,2), lt(4,1), cost(0,70,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), leafPos(1,3), scost(23,3,0), scost(23,3,1), posColor(2,green), lt(4,3), leafPos(2,1), scost(28,1,0), leafPos(3,4), scost(39,4,0), iterate(2,1), iterate(2,2), leafPos(4,0), scost(70,0,1)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,1), cost(3,23,0), cost(1,39,0), lt(4,1), cost(0,70,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), leafPos(1,3), scost(23,3,0), lt(4,3), scost(23,3,1), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(4,0), scost(70,0,1)}
{cost(0,81,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,1), lt(2,4), lt(2,1), cost(3,23,0), cost(1,45,0), lt(2,2), cost(0,81,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), leafPos(1,3), scost(23,3,0), lt(4,3), leafPos(2,0), scost(23,3,1), scost(81,0,1), iterate(2,1), iterate(2,2), posColor(2,green), leafPos(4,1), scost(45,1,0), leafPos(3,4), scost(39,4,0)}
{cost(0,70,0), cost(4,23,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), cost(3,28,1), lt(2,4), cost(3,28,0), cost(1,39,0), lt(4,1), cost(0,70,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), lt(4,3), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,3), scost(28,3,0), scost(28,3,1), leafPos(3,1), lt(3,3), scost(39,1,0), leafPos(4,0), scost(70,0,1), leafPos(1,4), scost(23,4,0)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), cost(3,28,1), lt(2,4), cost(3,28,0), lt(1,3), cost(1,45,0), lt(1,2), cost(0,53,1), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), lt(4,3), posColor(2,green), iterate(2,1), iterate(2,2), leafPos(2,3), leafPos(3,4), scost(28,3,0), scost(39,4,0), scost(28,3,1), leafPos(1,0), leafPos(4,1), scost(53,0,1), scost(45,1,0)}
{cost(0,53,0), cost(4,28,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(1,1), started(3,4), lt(1,3), cost(1,39,0), cost(2,45,0), started(3,3), lt(1,2), cost(0,53,1), cost(2,70,0), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), iterate(3,1), lt(4,3), posColor(2,green), posColor(3,green), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(1,0), leafPos(4,2), scost(53,0,1), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3)}
{cost(0,70,0), cost(4,28,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(1,3), cost(1,39,0), lt(4,1), cost(0,70,1), cost(2,53,0), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), iterate(3,1), lt(4,3), posColor(2,green), posColor(3,green), leafPos(1,2), scost(23,2,0), scost(53,2,0), leafPos(2,4), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(4,0), scost(70,0,1)}
{cost(0,70,0), cost(4,39,0), posColor(4,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(1,3), cost(1,28,0), lt(2,2), lt(4,1), cost(0,70,1), cost(2,53,0), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), leafPos(2,1), lt(4,3), scost(28,1,0), posColor(2,green), leafPos(3,4), scost(39,4,0), posColor(3,green), leafPos(1,2), scost(23,2,0), scost(53,2,0), leafPos(4,0), scost(70,0,1)}
{cost(0,53,0), cost(4,39,0), posColor(4,blue), started(1,4), started(1,3), posColor(1,blue), lt(1,4), lt(1,1), started(3,4), lt(2,4), lt(1,3), cost(1,28,0), cost(2,45,0), started(3,3), lt(2,2), lt(1,2), cost(0,53,1), cost(2,70,0), lt(4,4), lt(2,3), iterate(0,1), iterate(3,1), leafPos(2,1), lt(4,3), scost(28,1,0), posColor(2,green), leafPos(3,4), scost(39,4,0), posColor(3,green), leafPos(1,0), scost(53,0,1), leafPos(4,2), scost(70,2,0), starting(4), scost(45,2,0), started(2,4), started(2,3)}
{cost(0,70,0), cost(4,39,0), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(1,3), cost(1,28,0), cost(4,51,0), lt(2,2), lt(4,1), cost(0,70,1), cost(2,53,0), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(2,1), scost(28,1,0), lt(4,3), posColor(3,green), leafPos(1,2), scost(23,2,0), leafPos(4,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), posColor(2,green), scost(53,2,0), scost(70,0,1)}
{cost(0,51,0), cost(4,23,0), posColor(3,blue), posColor(1,blue), lt(2,4), cost(3,28,0), cost(1,45,0), cost(4,53,0), lt(3,1), cost(0,51,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), posColor(2,green), lt(4,3), scost(51,0,1), leafPos(3,0), lt(3,3), leafPos(2,3), scost(28,3,0), iterate(2,1), leafPos(4,1), scost(45,1,0), leafPos(1,4), scost(23,4,0), scost(53,4,0)}
{cost(0,70,0), cost(4,23,0), posColor(3,blue), posColor(1,blue), lt(2,4), cost(3,28,0), cost(1,39,0), cost(4,53,0), lt(4,1), cost(0,70,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), lt(4,3), leafPos(2,3), scost(28,3,0), iterate(2,1), posColor(2,green), leafPos(4,0), leafPos(3,1), scost(70,0,1), lt(3,3), scost(39,1,0), leafPos(1,4), scost(23,4,0), scost(53,4,0)}
{cost(0,53,0), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(1,45,0), cost(4,51,0), lt(1,2), cost(0,53,1), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), lt(4,3), leafPos(4,1), scost(45,1,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(1,0), scost(53,0,1), leafPos(2,3), scost(28,3,0), iterate(2,1), posColor(2,green)}
{cost(0,70,0), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), cost(4,51,0), lt(4,1), lt(1,2), cost(0,70,1), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), lt(4,3), leafPos(1,1), scost(23,1,0), leafPos(2,3), scost(28,3,0), leafPos(3,4), scost(51,4,0), scost(39,4,0), posColor(2,green), leafPos(4,0), scost(70,0,1), iterate(2,1)}
{cost(0,53,0), cost(4,45,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), cost(3,28,0), lt(1,3), cost(1,39,0), cost(4,70,0), lt(1,2), cost(0,53,1), lt(3,2), lt(3,4), iterate(0,1), posColor(4,green), leafPos(2,3), scost(28,3,0), posColor(2,green), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(1,0), scost(53,0,1), iterate(2,1)}
{cost(0,51,0), cost(4,45,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(3,28,0), cost(1,23,0), lt(1,3), cost(4,70,0), lt(3,1), cost(0,51,1), lt(1,2), lt(3,2), lt(3,4), iterate(0,1), posColor(4,green), leafPos(2,3), scost(28,3,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), lt(3,3), posColor(2,green), leafPos(3,0), scost(51,0,1), leafPos(1,1), scost(23,1,0), iterate(2,1)}
{cost(0,51,0), cost(4,23,0), posColor(3,blue), posColor(1,blue), lt(2,4), cost(1,28,0), cost(4,53,0), cost(3,45,0), lt(3,1), cost(0,51,1), lt(2,2), lt(3,2), lt(3,4), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), posColor(2,green), leafPos(3,0), lt(3,3), scost(51,0,1), iterate(2,1), leafPos(4,3), scost(45,3,0), leafPos(1,4), scost(23,4,0), scost(53,4,0), leafPos(2,1), scost(28,1,0)}
{cost(0,51,0), cost(4,28,0), posColor(3,blue), posColor(1,blue), lt(1,4), cost(1,23,0), lt(1,3), cost(4,81,0), cost(3,45,0), lt(3,1), cost(0,51,1), lt(1,2), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), posColor(4,green), posColor(2,green), scost(51,0,1), leafPos(3,0), lt(3,3), iterate(2,1), leafPos(1,1), leafPos(4,3), scost(23,1,0), scost(45,3,0), leafPos(2,4), scost(81,4,0), scost(28,4,0)}
{cost(0,51,0), cost(4,45,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(3,23,0), cost(1,28,0), cost(4,70,0), lt(3,1), cost(0,51,1), lt(2,2), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), posColor(4,green), posColor(2,green), scost(51,0,1), leafPos(3,0), lt(3,3), iterate(2,1), leafPos(1,3), scost(23,3,0), leafPos(4,4), scost(45,4,0), scost(70,4,0), leafPos(2,1), scost(28,1,0)}
{cost(0,53,0), cost(4,28,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(1,3), cost(1,39,0), cost(4,81,0), cost(3,45,0), lt(1,2), cost(0,53,1), lt(3,2), lt(3,4), lt(4,4), iterate(0,1), posColor(4,green), posColor(2,green), iterate(2,1), leafPos(4,3), scost(45,3,0), leafPos(3,1), lt(3,3), scost(39,1,0), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(1,0), scost(53,0,1)}
{cost(0,53,0), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(1,1), lt(2,4), lt(1,3), cost(1,28,0), cost(4,51,0), cost(3,45,0), lt(2,2), lt(1,2), cost(0,53,1), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(4,3), scost(45,3,0), posColor(2,green), iterate(2,1), leafPos(3,4), scost(51,4,0), scost(39,4,0), leafPos(2,1), scost(28,1,0), leafPos(1,0), scost(53,0,1)}
{posColor(2,blue), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), cost(2,23,0), lt(2,4), lt(1,3), cost(1,28,0), cost(4,51,0), cost(3,45,0), cost(1,28,1), cost(2,23,1), lt(2,2), cost(1,28,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(4,3), scost(45,3,0), iterate(1,1), iterate(0,2), scost(23,2,0), leafPos(1,2), leafPos(2,1), scost(28,1,0), scost(28,1,1), leafPos(3,4), scost(51,4,0), scost(39,4,0), iterate(2,1), scost(23,2,1), iterate(1,2), iterate(0,3), scost(28,1,2)}
{cost(0,70,0), cost(4,28,0), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,0), cost(1,39,0), cost(4,81,0), lt(4,1), cost(0,70,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), leafPos(1,3), scost(23,3,0), lt(4,3), posColor(2,green), leafPos(2,4), scost(81,4,0), scost(28,4,0), lt(3,3), leafPos(3,1), scost(39,1,0), leafPos(4,0), scost(70,0,1), iterate(2,1)}
{cost(0,81,0), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(1,45,0), cost(4,51,0), lt(2,2), cost(0,81,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), lt(4,3), leafPos(1,3), scost(23,3,0), posColor(2,green), leafPos(2,0), scost(81,0,1), iterate(2,1), leafPos(4,1), scost(45,1,0), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{cost(0,70,0), cost(4,39,0), posColor(1,blue), lt(1,4), lt(2,4), cost(3,23,0), cost(1,28,0), cost(4,51,0), lt(2,2), lt(4,1), cost(0,70,1), cost(3,53,0), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), lt(4,3), leafPos(1,3), scost(23,3,0), posColor(2,green), leafPos(2,1), scost(28,1,0), leafPos(4,0), scost(70,0,1), leafPos(3,4), scost(51,4,0), scost(39,4,0), posColor(3,green), scost(53,3,0)}
{cost(0,70,0), cost(4,39,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), cost(3,23,0), cost(1,28,0), cost(4,51,0), lt(2,2), lt(4,1), cost(0,70,1), lt(4,2), lt(4,4), lt(2,3), iterate(0,1), posColor(4,green), lt(4,3), leafPos(1,3), scost(23,3,0), posColor(2,green), leafPos(2,1), iterate(2,1), scost(28,1,0), leafPos(4,0), scost(70,0,1), leafPos(3,4), scost(51,4,0), scost(39,4,0)}
{cost(0,51,0), cost(4,28,0), posColor(3,blue), posColor(1,blue), lt(1,4), cost(3,23,0), cost(1,45,0), cost(4,81,0), lt(3,1), cost(0,51,1), lt(3,2), lt(3,4), lt(4,2), lt(4,4), iterate(0,1), posColor(4,green), lt(4,3), leafPos(1,3), scost(23,3,0), scost(51,0,1), leafPos(3,0), lt(3,3), posColor(2,green), iterate(2,1), leafPos(2,4), scost(81,4,0), scost(28,4,0), leafPos(4,1), scost(45,1,0)}
{cost(0,81,0), cost(4,45,0), posColor(3,blue), posColor(1,blue), lt(1,4), lt(2,4), lt(2,1), cost(3,23,0), cost(1,39,0), cost(4,70,0), lt(2,2), cost(0,81,1), lt(3,2), lt(3,4), lt(2,3), iterate(0,1), posColor(4,green), leafPos(1,3), scost(23,3,0), leafPos(4,4), lt(3,3), scost(45,4,0), scost(70,4,0), leafPos(3,1), scost(39,1,0), leafPos(2,0), scost(81,0,1), iterate(2,1), posColor(2,green)}
"""
