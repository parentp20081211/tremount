@namespace
class SpriteKind:
    Hitbox = SpriteKind.create()
    Slope = SpriteKind.create()
    Title = SpriteKind.create()
def game2():
    scene.set_background_image(assets.image("""
        forest
        """))
    scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
        assets.image("""
            clouds
            """))
    scroller.set_layer_image(scroller.BackgroundLayer.LAYER4,
        assets.image("""
            trees_parallax
            """))
    scroller.scroll_background_with_camera(scroller.CameraScrollMode.ONLY_HORIZONTAL,
        scroller.BackgroundLayer.LAYER4)
    scroller.scroll_background_with_speed(20, 0)
    tiles.set_current_tilemap(tilemap("""
        niveau0
        """))
    player2()
    physics.set_ignore([assets.tile("""
                short_grass
                """),
            assets.tile("""
                flowers_tile
                """),
            assets.tile("""
                wood_log
                """)])
    characterAnimations.set_character_state(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
    idle(mySprite4)
    tiles.place_on_tile(mySprite4, tiles.get_tile_location(2, 9))
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(2, 9))

def on_up_pressed():
    look_up()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def title_screen():
    pass
def walk_left():
    pass
def look_up():
    if characterAnimations.matches_rule(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT)):
        animation.run_image_animation(mySprite4,
            assets.animation("""
                look_up_right
                """),
            500,
            False)
    if characterAnimations.matches_rule(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT)):
        animation.run_image_animation(mySprite4,
            assets.animation("""
                look_up_left
                """),
            500,
            False)
def SpawnTextsprite(txt: str, X: number, Y: number):
    global Note2, textSprite
    Note2 = "Render's A Floating Text! "
    textSprite = textsprite.create(txt)
    textSprite.x = X
    textSprite.y = Y
    textSprite.set_outline(1, 15)

def on_b_pressed():
    if spriteutils.is_destroyed(TitleScreen):
        pass
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global jump
    jump = 0
    characterAnimations.set_character_state(mySprite4, characterAnimations.rule(Predicate.MOVING_UP))
    jump_in_air()
    animation.run_image_animation(mySprite4,
        assets.animation("""
            roll_anim
            """),
        500,
        False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    idle(mySprite4)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def walk():
    characterAnimations.loop_frames(mySprite4,
        assets.animation("""
            walking_left
            """),
        150,
        characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.FACING_LEFT))
    characterAnimations.loop_frames(mySprite4,
        assets.animation("""
            walking
            """),
        150,
        characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.FACING_RIGHT))

def on_left_pressed():
    characterAnimations.clear_character_state(mySprite4)
    characterAnimations.set_character_state(mySprite4,
        characterAnimations.rule(Predicate.FACING_LEFT, Predicate.MOVING_LEFT))
    walk()
    if characterAnimations.matches_rule(mySprite4, characterAnimations.rule(Predicate.MOVING_UP)):
        characterAnimations.set_character_state(mySprite4,
            characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT))
        animation.run_image_animation(mySprite4,
            assets.animation("""
                roll_anim
                """),
            500,
            False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    characterAnimations.set_character_state(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
    idle(mySprite4)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    characterAnimations.set_character_state(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
    idle(mySprite4)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def falling():
    if mySprite2.vy > 0:
        if mySprite2.vy > 200:
            characterAnimations.loop_frames(mySprite4,
                assets.animation("""
                    falling_anim0
                    """),
                500,
                characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
            characterAnimations.loop_frames(mySprite4,
                assets.animation("""
                    falling_anim
                    """),
                500,
                characterAnimations.rule(Predicate.NOT_MOVING, Predicate.MOVING_RIGHT))
def slope():
    global mySprite3
    mySprite3 = sprites.create(assets.image("""
        slope_right
        """), SpriteKind.Slope)
    tileUtil.create_sprites_on_tiles(assets.tile("""
            myTile
            """),
        assets.image("""
            slope_right
            """),
        SpriteKind.Slope)
    mySprite3.set_flag(SpriteFlag.SHOW_PHYSICS, True)
def moving_up():
    characterAnimations.loop_frames(mySprite4,
        assets.animation("""
            falling_anim
            """),
        500,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT))
    characterAnimations.loop_frames(mySprite4,
        assets.animation("""
            falling_anim0
            """),
        500,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT))

def on_right_pressed():
    characterAnimations.clear_character_state(mySprite4)
    characterAnimations.set_character_state(mySprite4,
        characterAnimations.rule(Predicate.FACING_RIGHT, Predicate.MOVING_RIGHT))
    walk()
    if characterAnimations.matches_rule(mySprite4, characterAnimations.rule(Predicate.MOVING_UP)):
        characterAnimations.set_character_state(mySprite4,
            characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT))
        animation.run_image_animation(mySprite4,
            assets.animation("""
                roll_anim
                """),
            500,
            False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    idle(mySprite4)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def moving_down():
    while mySprite2.is_hitting_tile(CollisionDirection.BOTTOM) == False:
        characterAnimations.loop_frames(mySprite4,
            assets.animation("""
                falling_anim
                """),
            500,
            characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(mySprite4,
            assets.animation("""
                falling_anim0
                """),
            500,
            characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))

def on_down_pressed():
    crouch()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def TransitionFadeToBlack(Time: number):
    global Note2
    Note2 = "Fades the screen To all black!"
    color.start_fade(color.original_palette, color.black, Time / 2)
    color.pause_until_fade_done()
    color.start_fade(color.black, color.original_palette, Time / 2)
def status_bar():
    global statusbar
    statusbar = statusbars.create(35, 8, StatusBarKind.health)
    statusbar.position_direction(CollisionDirection.BOTTOM)
    statusbar.set_label("HP")
def TransitionFadeToWhite(Time2: number):
    global Note2
    Note2 = "Fades the screen To all white!"
    color.start_fade(color.original_palette, color.white, Time2 / 2)
    color.pause_until_fade_done()
    color.start_fade(color.white, color.original_palette, Time2 / 2)
def player2():
    global mySprite4, mySprite2
    mySprite4 = sprites.create(assets.image("""
        ambedge
        """), SpriteKind.player)
    mySprite2 = sprites.create(assets.image("""
        hitbox0
        """), SpriteKind.Hitbox)
    controller.move_sprite(mySprite2, 100, 0)
    mySprite2.vy = 200
    scene.camera_follow_sprite(mySprite2)
    mySprite4.set_flag(SpriteFlag.GHOST, True)
    mySprite2.set_flag(SpriteFlag.INVISIBLE, True)
    physics.add_physics(mySprite2)
    status_bar()
def idle(mySprite: Sprite):
    if characterAnimations.matches_rule(mySprite,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT)):
        animation.run_image_animation(mySprite,
            assets.animation("""
                idle_left
                """),
            500,
            False)
    if characterAnimations.matches_rule(mySprite,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT)):
        animation.run_image_animation(mySprite, assets.animation("""
            idle
            """), 500, False)
def StartGame():
    pass

def on_combos_attach_combo():
    pass
controller.combos.attach_combo("l+r", on_combos_attach_combo)

def jump_in_air():
    if mySprite2.vy == 0:
        physics.gravity_ay(-200)
        
        def on_after():
            if controller.A.is_pressed():
                pass
            else:
                physics.gravity_ay(200)
        timer.after(250, on_after)
        
        
        def on_after2():
            physics.gravity_ay(350)
        timer.after(500, on_after2)
        
def walk_right():
    pass
def crouch():
    if characterAnimations.matches_rule(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT)):
        animation.run_image_animation(mySprite4,
            assets.animation("""
                crouch_right
                """),
            50,
            False)
    if characterAnimations.matches_rule(mySprite4,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT)):
        animation.run_image_animation(mySprite4,
            assets.animation("""
                crouch_left
                """),
            50,
            False)
statusbar: StatusBarSprite = None
mySprite3: Sprite = None
jump = 0
textSprite: TextSprite = None
mySprite2: Sprite = None
mySprite4: Sprite = None
TitleScreen: Sprite = None
Note2 = ""
Note2 = "Edit Any Number Values To Fit your liking"
TransitionFadeToWhite(1000)
scene.set_background_image(assets.image("""
    forest_for_that_other_game
    """))
TitleScreen = sprites.create(assets.image("""
    title_screen
    """), SpriteKind.Title)
animation.run_image_animation(TitleScreen,
    assets.animation("""
        title_screen animation
        """),
    500,
    True)
Note2 = "Draw Your Title Screen Above!"
SpawnTextsprite("Press B", 76, 110)
Note2 = "You Can Add Music Here!"

def on_after3():
    global Note2
    
    def on_pause_until():
        pass
    pause_until(on_pause_until)
    
    Note2 = "If music is playing, Put a stop all sounds block Here!"
    TransitionFadeToBlack(2000)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Title)
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    Note2 = "This Will Start The Game!"
    game2()
timer.after(2000, on_after3)

def on_on_update():
    if spriteutils.is_destroyed(TitleScreen):
        mySprite4.set_position(mySprite2.x, mySprite2.y)
game.on_update(on_on_update)

def on_on_update2():
    global jump
    if spriteutils.is_destroyed(TitleScreen):
        if mySprite2.vx == 0 and mySprite2.vy == 0:
            if mySprite2.is_hitting_tile(CollisionDirection.BOTTOM) == True:
                jump = 1
                idle(mySprite4)
game.on_update(on_on_update2)

def on_forever():
    pass
forever(on_forever)

def on_forever2():
    pass
forever(on_forever2)
