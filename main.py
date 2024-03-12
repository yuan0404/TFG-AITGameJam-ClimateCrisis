@namespace
class SpriteKind:
    object2 = SpriteKind.create()
    button = SpriteKind.create()

def on_b_pressed():
    global speed_record, sandbag, _delete
    speed_record = sandbag_shooter.vx
    sandbag_shooter.set_velocity(0, 0)
    sandbag = sprites.create_projectile_from_sprite(assets.image("""
        sandbag
    """), sandbag_shooter, 0, -150)
    if sandbag.x >= 57 and sandbag.x <= 103:
        pause(250)
        sandbag.set_velocity(0, 0)
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 1)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 2)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 3)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 4)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 5)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 6)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x + 7)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 1)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 2)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 3)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 4)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 5)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 6)))
        _delete = sandbag_record.remove_at(sandbag_record.index(Math.round(sandbag.x - 7)))
    pause(1000)
    sandbag_shooter.set_velocity(speed_record, 0)
    if len(sandbag_record) == 0:
        game.over(True)
    else:
        scene.set_background_image(wall_list[wall_list.index(scene.background_image()) + 1])
        if scene.background_image() == wall_list[10]:
            pause(500)
            game.over(False)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def game_3():
    global mouse
    scene.set_background_image(assets.image("""
        game rule 3
    """))
    pause(3000)
    set_background()
    mouse = sprites.create(assets.image("""
        mouse
    """), SpriteKind.player)
    mouse.set_stay_in_screen(True)
    mouse.set_position(80, 73)
    controller.move_sprite(mouse)
    info.start_countdown(30)
def set_background():
    global pipe_record, pipe_check, pipe_1_1, pipe_1_2, pipe_1_3, pipe_1_4, pipe_1_5, pipe_2_1, pipe_2_2, pipe_2_3, pipe_2_4, pipe_2_5, pipe_3_1, pipe_3_2, pipe_3_3, pipe_3_4, pipe_3_5, pipe_4_1, pipe_4_2, pipe_4_3, pipe_4_4, pipe_4_5, pipe_start
    pipe_record = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pipe_check = [randint(0, 3),
        randint(0, 3),
        randint(0, 3),
        randint(0, 3),
        randint(0, 1),
        randint(0, 1),
        randint(0, 3),
        randint(0, 3),
        randint(0, 3),
        randint(0, 3),
        randint(0, 1),
        randint(0, 1),
        randint(0, 3),
        randint(0, 3)]
    scene.set_background_image(assets.image("""
        grass land
    """))
    pipe_1_1 = sprites.create(assets.image("""
        pipe L 4
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_1_1, -90 * pipe_check[0])
    pipe_1_1.set_position(28, 21)
    pipe_1_2 = sprites.create(assets.image("""
        pipe L 3
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_1_2, -90 * pipe_check[1])
    pipe_1_2.set_position(54, 21)
    pipe_1_3 = sprites.create(assets.image("""
        pipe L 4
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_1_3, -90 * pipe_check[2])
    pipe_1_3.set_position(80, 21)
    pipe_1_4 = sprites.create(assets.image("""
        pipe L 3
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_1_4, -90 * pipe_check[3])
    pipe_1_4.set_position(106, 21)
    pipe_1_5 = sprites.create(assets.image("""
        giraffe
    """), SpriteKind.object2)
    pipe_1_5.set_position(132, 21)
    pipe_2_1 = sprites.create(assets.image("""
        pipe I 2
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_2_1, -90 * pipe_check[4])
    pipe_2_1.set_position(28, 47)
    pipe_2_2 = sprites.create(assets.image("""
        pipe I 2
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_2_2, -90 * pipe_check[5])
    pipe_2_2.set_position(54, 47)
    pipe_2_3 = sprites.create(assets.image("""
        pipe L 2
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_2_3, -90 * pipe_check[6])
    pipe_2_3.set_position(80, 47)
    pipe_2_4 = sprites.create(assets.image("""
        pipe X
    """), SpriteKind.object2)
    pipe_2_4.set_position(106, 47)
    pipe_2_5 = sprites.create(assets.image("""
        pipe L 4
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_2_5, -90 * pipe_check[7])
    pipe_2_5.set_position(132, 47)
    pipe_3_1 = sprites.create(assets.image("""
        pipe L 2
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_3_1, -90 * pipe_check[8])
    pipe_3_1.set_position(28, 73)
    pipe_3_2 = sprites.create(assets.image("""
        pipe T
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_3_2, -90 * pipe_check[9])
    pipe_3_2.set_position(54, 73)
    pipe_3_3 = sprites.create(assets.image("""
        grass
    """), SpriteKind.object2)
    pipe_3_3.set_position(80, 73)
    pipe_3_4 = sprites.create(assets.image("""
        pipe I 2
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_3_4, -90 * pipe_check[10])
    pipe_3_4.set_position(106, 73)
    pipe_3_5 = sprites.create(assets.image("""
        pipe I 2
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_3_5, -90 * pipe_check[11])
    pipe_3_5.set_position(132, 73)
    pipe_4_1 = sprites.create(assets.image("""
        horse 1
    """), SpriteKind.object2)
    pipe_4_1.set_position(28, 99)
    pipe_4_2 = sprites.create(assets.image("""
        pipe L 1
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_4_2, -90 * pipe_check[12])
    pipe_4_2.set_position(54, 99)
    pipe_4_3 = sprites.create(assets.image("""
        antelope
    """), SpriteKind.object2)
    pipe_4_3.set_position(80, 99)
    pipe_4_4 = sprites.create(assets.image("""
        pipe L 1
    """), SpriteKind.object2)
    transformSprites.change_rotation(pipe_4_4, -90 * pipe_check[13])
    pipe_4_4.set_position(106, 99)
    pipe_4_5 = sprites.create(assets.image("""
        horse 2
    """), SpriteKind.object2)
    pipe_4_5.set_position(132, 99)
    pipe_start = sprites.create(assets.image("""
        pipe start
    """), SpriteKind.player)
    pipe_start.set_position(10, 14)
def decide_game():
    global game1, game2, game3, exit2, mouse_start
    scene.set_background_image(assets.image("""
        結尾
    """))
    game1 = sprites.create(assets.image("""
        button 1-1
    """), SpriteKind.button)
    game1.set_position(80, 29)
    game2 = sprites.create(assets.image("""
        button 2-1
    """), SpriteKind.button)
    game2.set_position(80, 53)
    game3 = sprites.create(assets.image("""
        button 3-1
    """), SpriteKind.button)
    game3.set_position(80, 77)
    exit2 = sprites.create(assets.image("""
        button 4-1
    """), SpriteKind.button)
    exit2.set_position(80, 101)
    mouse_start = sprites.create(assets.image("""
        mouse start
    """), SpriteKind.player)
    mouse_start.set_position(108, 20)
    controller.move_sprite(mouse_start, 0, 100)
def end():
    scene.set_background_image(assets.image("""
        Ending
    """))
    pause(30000)
    game.reset()
def game_start():
    global earth, earth_list
    earth = sprites.create(assets.image("""
        earth 1
    """), SpriteKind.player)
    earth_list = [assets.image("""
            earth 1
        """),
        assets.image("""
            earth 2
        """)]
    animation.run_image_animation(earth,
        [assets.image("""
                earth 1
            """),
            assets.image("""
                earth 2
            """)],
        500,
        True)
def game_2():
    global iceland, ice, penguin
    scene.set_background_image(assets.image("""
        game rule 2
    """))
    pause(3000)
    scene.set_background_image(assets.image("""
        south pole
    """))
    effects.blizzard.start_screen_effect()
    iceland = sprites.create(assets.image("""
        ice land
    """), SpriteKind.player)
    ice = sprites.create(assets.image("""
        ice
    """), SpriteKind.player)
    penguin = sprites.create(assets.image("""
        penguin
    """), SpriteKind.player)
    penguin.set_stay_in_screen(True)
    penguin.set_position(80, 61)
    iceland.set_position(80, 70)
    info.set_life(5)
    while info.life() > 0:
        if True:
            controller.move_sprite(penguin, randint(20, 100), 0)
            ice.set_position(randint(20, 140), 0)
            ice.set_velocity(0, 50)
            pause(1000)
            if ice.overlaps_with(penguin):
                info.change_life_by(1)
                iceland.change_scale(0.2, ScaleAnchor.MIDDLE)
            else:
                pause(3000)
                info.change_life_by(-1)
                iceland.change_scale(-0.2, ScaleAnchor.MIDDLE)
            if info.life() == 10:
                pause(200)
                game.over(True)
        else:
            game.over(False)

def on_countdown_end():
    game.over(False)
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    if mouse_start.overlaps_with(game1):
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit2.destroy()
        mouse_start.destroy()
        game_1()
    elif mouse_start.overlaps_with(game2):
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit2.destroy()
        mouse_start.destroy()
        game_2()
    elif mouse_start.overlaps_with(game3):
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit2.destroy()
        mouse_start.destroy()
        game_3()
    elif mouse_start.overlaps_with(exit2):
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit2.destroy()
        mouse_start.destroy()
        end()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    if mouse_start.overlaps_with(game1):
        game1.set_image(assets.image("""
            button 1-0
        """))
    else:
        game1.set_image(assets.image("""
            button 1-1
        """))
    if mouse_start.overlaps_with(game2):
        game2.set_image(assets.image("""
            button 2-2
        """))
    else:
        game2.set_image(assets.image("""
            button 2-1
        """))
    if mouse_start.overlaps_with(game3):
        game3.set_image(assets.image("""
            button 3-2
        """))
    else:
        game3.set_image(assets.image("""
            button 3-1
        """))
    if mouse_start.overlaps_with(exit2):
        exit2.set_image(assets.image("""
            button 4-2
        """))
    else:
        exit2.set_image(assets.image("""
            button 4-1
        """))
sprites.on_overlap(SpriteKind.player, SpriteKind.button, on_on_overlap)

def game_1():
    global sandbag_shooter, sandbag_record, wall_list
    scene.set_background_image(assets.image("""
        game rule 1
    """))
    pause(3000)
    scene.set_background_image(assets.image("""
        wall
    """))
    sandbag_shooter = sprites.create(assets.image("""
        shooter
    """), SpriteKind.player)
    sandbag_shooter.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
    sandbag_shooter.set_position(80, 100)
    sandbag_shooter.set_velocity(200, 0)
    sandbag_record = [62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98]
    wall_list = [assets.image("""
            wall 1
        """),
        assets.image("""
            wall 2
        """),
        assets.image("""
            wall 3
        """),
        assets.image("""
            wall 4
        """),
        assets.image("""
            wall 5
        """),
        assets.image("""
            wall 6
        """),
        assets.image("""
            wall 7
        """),
        assets.image("""
            wall 8
        """),
        assets.image("""
            wall 9
        """),
        assets.image("""
            wall 10
        """),
        assets.image("""
            wall 11
        """)]

def on_a_pressed():
    if mouse.overlaps_with(pipe_1_1):
        transformSprites.change_rotation(pipe_1_1, 90)
        pipe_record[0] = (pipe_record[0] + 1) % 4
    if mouse.overlaps_with(pipe_1_2):
        transformSprites.change_rotation(pipe_1_2, 90)
        pipe_record[1] = (pipe_record[1] + 1) % 4
    if mouse.overlaps_with(pipe_1_3):
        transformSprites.change_rotation(pipe_1_3, 90)
        pipe_record[2] = (pipe_record[2] + 1) % 4
    if mouse.overlaps_with(pipe_1_4):
        transformSprites.change_rotation(pipe_1_4, 90)
        pipe_record[3] = (pipe_record[3] + 1) % 4
    if mouse.overlaps_with(pipe_2_1):
        if (pipe_record[4] + 1) % 2 == pipe_check[4]:
            transformSprites.change_rotation(pipe_2_1, 90)
            pipe_record[4] = (pipe_record[4] + 1) % 2
        else:
            transformSprites.change_rotation(pipe_2_1, -90)
            pipe_record[4] = (pipe_record[4] + 1) % 2
    if mouse.overlaps_with(pipe_2_2):
        if (pipe_record[5] + 1) % 2 == pipe_check[5]:
            transformSprites.change_rotation(pipe_2_2, 90)
            pipe_record[5] = (pipe_record[5] + 1) % 2
        else:
            transformSprites.change_rotation(pipe_2_2, -90)
            pipe_record[5] = (pipe_record[5] + 1) % 2
    if mouse.overlaps_with(pipe_2_3):
        transformSprites.change_rotation(pipe_2_3, 90)
        pipe_record[6] = (pipe_record[6] + 1) % 4
    if mouse.overlaps_with(pipe_2_5):
        transformSprites.change_rotation(pipe_2_5, 90)
        pipe_record[7] = (pipe_record[7] + 1) % 4
    if mouse.overlaps_with(pipe_3_1):
        transformSprites.change_rotation(pipe_3_1, 90)
        pipe_record[8] = (pipe_record[8] + 1) % 4
    if mouse.overlaps_with(pipe_3_2):
        transformSprites.change_rotation(pipe_3_2, 90)
        pipe_record[9] = (pipe_record[9] + 1) % 4
    if mouse.overlaps_with(pipe_3_4):
        if (pipe_record[10] + 1) % 2 == pipe_check[10]:
            transformSprites.change_rotation(pipe_3_4, 90)
            pipe_record[10] = (pipe_record[10] + 1) % 2
        else:
            transformSprites.change_rotation(pipe_3_4, -90)
            pipe_record[10] = (pipe_record[10] + 1) % 2
    if mouse.overlaps_with(pipe_3_5):
        if (pipe_record[11] + 1) % 2 == pipe_check[11]:
            transformSprites.change_rotation(pipe_3_5, 90)
            pipe_record[11] = (pipe_record[11] + 1) % 2
        else:
            transformSprites.change_rotation(pipe_3_5, -90)
            pipe_record[11] = (pipe_record[11] + 1) % 2
    if mouse.overlaps_with(pipe_4_2):
        transformSprites.change_rotation(pipe_4_2, 90)
        pipe_record[12] = (pipe_record[12] + 1) % 4
    if mouse.overlaps_with(pipe_4_4):
        transformSprites.change_rotation(pipe_4_4, 90)
        pipe_record[13] = (pipe_record[13] + 1) % 4
    if pipe_record[0] == pipe_check[0]:
        if pipe_record[1] == pipe_check[1]:
            if pipe_record[2] == pipe_check[2]:
                if pipe_record[3] == pipe_check[3]:
                    if pipe_record[4] == pipe_check[4]:
                        if pipe_record[5] == pipe_check[5]:
                            if pipe_record[6] == pipe_check[6]:
                                if pipe_record[7] == pipe_check[7]:
                                    if pipe_record[8] == pipe_check[8]:
                                        if pipe_record[9] == pipe_check[9]:
                                            if pipe_record[10] == pipe_check[10]:
                                                if pipe_record[11] == pipe_check[11]:
                                                    if pipe_record[12] == pipe_check[12]:
                                                        if pipe_record[13] == pipe_check[13]:
                                                            pause(500)
                                                            pipe_1_1.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_1_2.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_1_3.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_1_4.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_2_1.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_2_2.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_2_3.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_2_4.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_2_5.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_3_1.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_3_2.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_3_4.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_3_5.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_4_2.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_4_4.change_scale(0.1, ScaleAnchor.MIDDLE)
                                                            pipe_start.change_scale(0, ScaleAnchor.MIDDLE)
                                                            info.stop_countdown()
                                                            pause(1000)
                                                            game.over(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

penguin: Sprite = None
ice: Sprite = None
iceland: Sprite = None
earth_list: List[Image] = []
mouse_start: Sprite = None
exit2: Sprite = None
game3: Sprite = None
game2: Sprite = None
game1: Sprite = None
pipe_start: Sprite = None
pipe_4_5: Sprite = None
pipe_4_4: Sprite = None
pipe_4_3: Sprite = None
pipe_4_2: Sprite = None
pipe_4_1: Sprite = None
pipe_3_5: Sprite = None
pipe_3_4: Sprite = None
pipe_3_3: Sprite = None
pipe_3_2: Sprite = None
pipe_3_1: Sprite = None
pipe_2_5: Sprite = None
pipe_2_4: Sprite = None
pipe_2_3: Sprite = None
pipe_2_2: Sprite = None
pipe_2_1: Sprite = None
pipe_1_5: Sprite = None
pipe_1_4: Sprite = None
pipe_1_3: Sprite = None
pipe_1_2: Sprite = None
pipe_1_1: Sprite = None
pipe_check: List[number] = []
pipe_record: List[number] = []
mouse: Sprite = None
wall_list: List[Image] = []
sandbag_record: List[number] = []
_delete = 0
sandbag: Sprite = None
sandbag_shooter: Sprite = None
speed_record = 0
earth: Sprite = None
scene.set_background_color(6)
game_start()
climate_change = sprites.create(assets.image("""
    Title
"""), SpriteKind.object2)
pause(3000)
climate_change.destroy()
earth.destroy()
decide_game()