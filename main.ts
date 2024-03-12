namespace SpriteKind {
    export const object = SpriteKind.create()
    export const button = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    speed_record = sandbag_shooter.vx
    sandbag_shooter.setVelocity(0, 0)
    sandbag = sprites.createProjectileFromSprite(assets.image`sandbag`, sandbag_shooter, 0, -150)
    if (sandbag.x >= 57 && sandbag.x <= 103) {
        pause(250)
        sandbag.setVelocity(0, 0)
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 1)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 2)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 3)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 4)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 5)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 6)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x + 7)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 1)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 2)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 3)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 4)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 5)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 6)))
        _delete = sandbag_record.removeAt(sandbag_record.indexOf(Math.round(sandbag.x - 7)))
    }
    pause(1000)
    sandbag_shooter.setVelocity(speed_record, 0)
    if (sandbag_record.length == 0) {
        game.over(true)
    } else {
        scene.setBackgroundImage(wall_list[wall_list.indexOf(scene.backgroundImage()) + 1])
        if (scene.backgroundImage() == wall_list[10]) {
            pause(500)
            game.over(false)
        }
    }
})
function game_3 () {
    scene.setBackgroundImage(assets.image`game rule 3`)
    pause(3000)
    set_background()
    mouse = sprites.create(assets.image`mouse`, SpriteKind.Player)
    mouse.setStayInScreen(true)
    mouse.setPosition(80, 73)
    controller.moveSprite(mouse)
    info.startCountdown(30)
}
function set_background () {
    pipe_record = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
    ]
    pipe_check = [
    randint(0, 3),
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
    randint(0, 3)
    ]
    scene.setBackgroundImage(assets.image`grass land`)
    pipe_1_1 = sprites.create(assets.image`pipe L 4`, SpriteKind.object)
    transformSprites.changeRotation(pipe_1_1, -90 * pipe_check[0])
    pipe_1_1.setPosition(28, 21)
    pipe_1_2 = sprites.create(assets.image`pipe L 3`, SpriteKind.object)
    transformSprites.changeRotation(pipe_1_2, -90 * pipe_check[1])
    pipe_1_2.setPosition(54, 21)
    pipe_1_3 = sprites.create(assets.image`pipe L 4`, SpriteKind.object)
    transformSprites.changeRotation(pipe_1_3, -90 * pipe_check[2])
    pipe_1_3.setPosition(80, 21)
    pipe_1_4 = sprites.create(assets.image`pipe L 3`, SpriteKind.object)
    transformSprites.changeRotation(pipe_1_4, -90 * pipe_check[3])
    pipe_1_4.setPosition(106, 21)
    pipe_1_5 = sprites.create(assets.image`giraffe`, SpriteKind.object)
    pipe_1_5.setPosition(132, 21)
    pipe_2_1 = sprites.create(assets.image`pipe I 2`, SpriteKind.object)
    transformSprites.changeRotation(pipe_2_1, -90 * pipe_check[4])
    pipe_2_1.setPosition(28, 47)
    pipe_2_2 = sprites.create(assets.image`pipe I 2`, SpriteKind.object)
    transformSprites.changeRotation(pipe_2_2, -90 * pipe_check[5])
    pipe_2_2.setPosition(54, 47)
    pipe_2_3 = sprites.create(assets.image`pipe L 2`, SpriteKind.object)
    transformSprites.changeRotation(pipe_2_3, -90 * pipe_check[6])
    pipe_2_3.setPosition(80, 47)
    pipe_2_4 = sprites.create(assets.image`pipe X`, SpriteKind.object)
    pipe_2_4.setPosition(106, 47)
    pipe_2_5 = sprites.create(assets.image`pipe L 4`, SpriteKind.object)
    transformSprites.changeRotation(pipe_2_5, -90 * pipe_check[7])
    pipe_2_5.setPosition(132, 47)
    pipe_3_1 = sprites.create(assets.image`pipe L 2`, SpriteKind.object)
    transformSprites.changeRotation(pipe_3_1, -90 * pipe_check[8])
    pipe_3_1.setPosition(28, 73)
    pipe_3_2 = sprites.create(assets.image`pipe T`, SpriteKind.object)
    transformSprites.changeRotation(pipe_3_2, -90 * pipe_check[9])
    pipe_3_2.setPosition(54, 73)
    pipe_3_3 = sprites.create(assets.image`grass`, SpriteKind.object)
    pipe_3_3.setPosition(80, 73)
    pipe_3_4 = sprites.create(assets.image`pipe I 2`, SpriteKind.object)
    transformSprites.changeRotation(pipe_3_4, -90 * pipe_check[10])
    pipe_3_4.setPosition(106, 73)
    pipe_3_5 = sprites.create(assets.image`pipe I 2`, SpriteKind.object)
    transformSprites.changeRotation(pipe_3_5, -90 * pipe_check[11])
    pipe_3_5.setPosition(132, 73)
    pipe_4_1 = sprites.create(assets.image`horse 1`, SpriteKind.object)
    pipe_4_1.setPosition(28, 99)
    pipe_4_2 = sprites.create(assets.image`pipe L 1`, SpriteKind.object)
    transformSprites.changeRotation(pipe_4_2, -90 * pipe_check[12])
    pipe_4_2.setPosition(54, 99)
    pipe_4_3 = sprites.create(assets.image`antelope`, SpriteKind.object)
    pipe_4_3.setPosition(80, 99)
    pipe_4_4 = sprites.create(assets.image`pipe L 1`, SpriteKind.object)
    transformSprites.changeRotation(pipe_4_4, -90 * pipe_check[13])
    pipe_4_4.setPosition(106, 99)
    pipe_4_5 = sprites.create(assets.image`horse 2`, SpriteKind.object)
    pipe_4_5.setPosition(132, 99)
    pipe_start = sprites.create(assets.image`pipe start`, SpriteKind.Player)
    pipe_start.setPosition(10, 14)
}
function decide_game () {
    scene.setBackgroundImage(assets.image`結尾`)
    game1 = sprites.create(assets.image`button 1-1`, SpriteKind.button)
    game1.setPosition(80, 29)
    game2 = sprites.create(assets.image`button 2-1`, SpriteKind.button)
    game2.setPosition(80, 53)
    game3 = sprites.create(assets.image`button 3-1`, SpriteKind.button)
    game3.setPosition(80, 77)
    exit = sprites.create(assets.image`button 4-1`, SpriteKind.button)
    exit.setPosition(80, 101)
    mouse_start = sprites.create(assets.image`mouse start`, SpriteKind.Player)
    mouse_start.setPosition(108, 20)
    controller.moveSprite(mouse_start, 0, 100)
}
function end () {
    scene.setBackgroundImage(assets.image`Ending`)
    pause(30000)
    game.reset()
}
function game_start () {
    earth = sprites.create(assets.image`earth 1`, SpriteKind.Player)
    earth_list = [assets.image`earth 1`, assets.image`earth 2`]
    animation.runImageAnimation(
    earth,
    [assets.image`earth 1`, assets.image`earth 2`],
    500,
    true
    )
}
function game_2 () {
    scene.setBackgroundImage(assets.image`game rule 2`)
    pause(3000)
    scene.setBackgroundImage(assets.image`south pole`)
    effects.blizzard.startScreenEffect()
    iceland = sprites.create(assets.image`ice land`, SpriteKind.Player)
    ice = sprites.create(assets.image`ice`, SpriteKind.Player)
    penguin = sprites.create(assets.image`penguin`, SpriteKind.Player)
    penguin.setStayInScreen(true)
    penguin.setPosition(80, 61)
    iceland.setPosition(80, 70)
    info.setLife(5)
    while (info.life() > 0) {
        if (true) {
            controller.moveSprite(penguin, randint(20, 100), 0)
            ice.setPosition(randint(20, 140), 0)
            ice.setVelocity(0, 50)
            pause(1000)
            if (ice.overlapsWith(penguin)) {
                info.changeLifeBy(1)
                iceland.changeScale(0.2, ScaleAnchor.Middle)
            } else {
                pause(3000)
                info.changeLifeBy(-1)
                iceland.changeScale(-0.2, ScaleAnchor.Middle)
            }
            if (info.life() == 10) {
                pause(200)
                game.over(true)
            }
        } else {
            game.over(false)
        }
    }
}
info.onCountdownEnd(function () {
    game.over(false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mouse_start.overlapsWith(game1)) {
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit.destroy()
        mouse_start.destroy()
        game_1()
    } else if (mouse_start.overlapsWith(game2)) {
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit.destroy()
        mouse_start.destroy()
        game_2()
    } else if (mouse_start.overlapsWith(game3)) {
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit.destroy()
        mouse_start.destroy()
        game_3()
    } else if (mouse_start.overlapsWith(exit)) {
        game1.destroy()
        game2.destroy()
        game3.destroy()
        exit.destroy()
        mouse_start.destroy()
        end()
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.button, function (sprite, otherSprite) {
    if (mouse_start.overlapsWith(game1)) {
        game1.setImage(assets.image`button 1-0`)
    } else {
        game1.setImage(assets.image`button 1-1`)
    }
    if (mouse_start.overlapsWith(game2)) {
        game2.setImage(assets.image`button 2-2`)
    } else {
        game2.setImage(assets.image`button 2-1`)
    }
    if (mouse_start.overlapsWith(game3)) {
        game3.setImage(assets.image`button 3-2`)
    } else {
        game3.setImage(assets.image`button 3-1`)
    }
    if (mouse_start.overlapsWith(exit)) {
        exit.setImage(assets.image`button 4-2`)
    } else {
        exit.setImage(assets.image`button 4-1`)
    }
})
function game_1 () {
    scene.setBackgroundImage(assets.image`game rule 1`)
    pause(3000)
    scene.setBackgroundImage(assets.image`wall`)
    sandbag_shooter = sprites.create(assets.image`shooter`, SpriteKind.Player)
    sandbag_shooter.setFlag(SpriteFlag.BounceOnWall, true)
    sandbag_shooter.setPosition(80, 100)
    sandbag_shooter.setVelocity(200, 0)
    sandbag_record = [
    62,
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
    98
    ]
    wall_list = [
    assets.image`wall 1`,
    assets.image`wall 2`,
    assets.image`wall 3`,
    assets.image`wall 4`,
    assets.image`wall 5`,
    assets.image`wall 6`,
    assets.image`wall 7`,
    assets.image`wall 8`,
    assets.image`wall 9`,
    assets.image`wall 10`,
    assets.image`wall 11`
    ]
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mouse.overlapsWith(pipe_1_1)) {
        transformSprites.changeRotation(pipe_1_1, 90)
        pipe_record[0] = (pipe_record[0] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_1_2)) {
        transformSprites.changeRotation(pipe_1_2, 90)
        pipe_record[1] = (pipe_record[1] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_1_3)) {
        transformSprites.changeRotation(pipe_1_3, 90)
        pipe_record[2] = (pipe_record[2] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_1_4)) {
        transformSprites.changeRotation(pipe_1_4, 90)
        pipe_record[3] = (pipe_record[3] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_2_1)) {
        if ((pipe_record[4] + 1) % 2 == pipe_check[4]) {
            transformSprites.changeRotation(pipe_2_1, 90)
            pipe_record[4] = (pipe_record[4] + 1) % 2
        } else {
            transformSprites.changeRotation(pipe_2_1, -90)
            pipe_record[4] = (pipe_record[4] + 1) % 2
        }
    }
    if (mouse.overlapsWith(pipe_2_2)) {
        if ((pipe_record[5] + 1) % 2 == pipe_check[5]) {
            transformSprites.changeRotation(pipe_2_2, 90)
            pipe_record[5] = (pipe_record[5] + 1) % 2
        } else {
            transformSprites.changeRotation(pipe_2_2, -90)
            pipe_record[5] = (pipe_record[5] + 1) % 2
        }
    }
    if (mouse.overlapsWith(pipe_2_3)) {
        transformSprites.changeRotation(pipe_2_3, 90)
        pipe_record[6] = (pipe_record[6] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_2_5)) {
        transformSprites.changeRotation(pipe_2_5, 90)
        pipe_record[7] = (pipe_record[7] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_3_1)) {
        transformSprites.changeRotation(pipe_3_1, 90)
        pipe_record[8] = (pipe_record[8] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_3_2)) {
        transformSprites.changeRotation(pipe_3_2, 90)
        pipe_record[9] = (pipe_record[9] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_3_4)) {
        if ((pipe_record[10] + 1) % 2 == pipe_check[10]) {
            transformSprites.changeRotation(pipe_3_4, 90)
            pipe_record[10] = (pipe_record[10] + 1) % 2
        } else {
            transformSprites.changeRotation(pipe_3_4, -90)
            pipe_record[10] = (pipe_record[10] + 1) % 2
        }
    }
    if (mouse.overlapsWith(pipe_3_5)) {
        if ((pipe_record[11] + 1) % 2 == pipe_check[11]) {
            transformSprites.changeRotation(pipe_3_5, 90)
            pipe_record[11] = (pipe_record[11] + 1) % 2
        } else {
            transformSprites.changeRotation(pipe_3_5, -90)
            pipe_record[11] = (pipe_record[11] + 1) % 2
        }
    }
    if (mouse.overlapsWith(pipe_4_2)) {
        transformSprites.changeRotation(pipe_4_2, 90)
        pipe_record[12] = (pipe_record[12] + 1) % 4
    }
    if (mouse.overlapsWith(pipe_4_4)) {
        transformSprites.changeRotation(pipe_4_4, 90)
        pipe_record[13] = (pipe_record[13] + 1) % 4
    }
    if (pipe_record[0] == pipe_check[0]) {
        if (pipe_record[1] == pipe_check[1]) {
            if (pipe_record[2] == pipe_check[2]) {
                if (pipe_record[3] == pipe_check[3]) {
                    if (pipe_record[4] == pipe_check[4]) {
                        if (pipe_record[5] == pipe_check[5]) {
                            if (pipe_record[6] == pipe_check[6]) {
                                if (pipe_record[7] == pipe_check[7]) {
                                    if (pipe_record[8] == pipe_check[8]) {
                                        if (pipe_record[9] == pipe_check[9]) {
                                            if (pipe_record[10] == pipe_check[10]) {
                                                if (pipe_record[11] == pipe_check[11]) {
                                                    if (pipe_record[12] == pipe_check[12]) {
                                                        if (pipe_record[13] == pipe_check[13]) {
                                                            pause(500)
                                                            pipe_1_1.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_1_2.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_1_3.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_1_4.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_2_1.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_2_2.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_2_3.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_2_4.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_2_5.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_3_1.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_3_2.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_3_4.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_3_5.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_4_2.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_4_4.changeScale(0.1, ScaleAnchor.Middle)
                                                            pipe_start.changeScale(0, ScaleAnchor.Middle)
                                                            info.stopCountdown()
                                                            pause(1000)
                                                            game.over(true)
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
let penguin: Sprite = null
let ice: Sprite = null
let iceland: Sprite = null
let earth_list: Image[] = []
let mouse_start: Sprite = null
let exit: Sprite = null
let game3: Sprite = null
let game2: Sprite = null
let game1: Sprite = null
let pipe_start: Sprite = null
let pipe_4_5: Sprite = null
let pipe_4_4: Sprite = null
let pipe_4_3: Sprite = null
let pipe_4_2: Sprite = null
let pipe_4_1: Sprite = null
let pipe_3_5: Sprite = null
let pipe_3_4: Sprite = null
let pipe_3_3: Sprite = null
let pipe_3_2: Sprite = null
let pipe_3_1: Sprite = null
let pipe_2_5: Sprite = null
let pipe_2_4: Sprite = null
let pipe_2_3: Sprite = null
let pipe_2_2: Sprite = null
let pipe_2_1: Sprite = null
let pipe_1_5: Sprite = null
let pipe_1_4: Sprite = null
let pipe_1_3: Sprite = null
let pipe_1_2: Sprite = null
let pipe_1_1: Sprite = null
let pipe_check: number[] = []
let pipe_record: number[] = []
let mouse: Sprite = null
let wall_list: Image[] = []
let sandbag_record: number[] = []
let _delete = 0
let sandbag: Sprite = null
let sandbag_shooter: Sprite = null
let speed_record = 0
let earth: Sprite = null
scene.setBackgroundColor(6)
game_start()
let climate_change = sprites.create(assets.image`Title`, SpriteKind.object)
pause(3000)
climate_change.destroy()
earth.destroy()
decide_game()
