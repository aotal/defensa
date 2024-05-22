def embed_youtube(video_id, start, end, width=500, height=280, autoplay=1, mute=1, playback_speed=1.0):
    html_content = f"""
    <div id="player"></div>

    <script>
    var tag = document.createElement("script");
    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName("script")[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    var player;
    function onYouTubeIframeAPIReady() {{
      player = new YT.Player("player", {{
        height: "{height}",
        width: "{width}",
        videoId: "{video_id}",
        playerVars: {{
          autoplay: {autoplay},
          loop: 1,
          playlist: "{video_id}",
          mute: {mute}
        }},
        events: {{
          "onReady": onPlayerReady,
          "onStateChange": onPlayerStateChange
        }}
      }});
    }}

    function onPlayerReady(event) {{
      event.target.setPlaybackRate({playback_speed});
      event.target.seekTo({start});
      event.target.playVideo();
    }}

    function onPlayerStateChange(event) {{
      if (event.data == YT.PlayerState.PLAYING) {{
        setTimeout(checkTime, 1000);
      }}
    }}

    function checkTime() {{
      if (player.getCurrentTime() >= {end}) {{
        player.seekTo({start});
      }} else {{
        setTimeout(checkTime, 1000);
      }}
    }}
    </script>
    """
    return html_content
