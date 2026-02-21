playlist = eval(input("Enter playlist: "))

if any(duration <= 0 for duration in playlist):
    print("Invalid Playlist")
else:
    total = sum(playlist)
    songs = len(playlist)

    if total < 300:
        category = "Too Short Playlist"
        suggestion = "Add more songs"

    elif total > 3600:
        category = "Too Long Playlist"
        suggestion = "Consider shortening your playlist"

    elif any(playlist.count(duration) > 1 for duration in playlist):
        category = "Repetitive Playlist"
        suggestion = "Add variety"

    elif max(playlist) - min(playlist) <= 300:
        category = "Balanced Playlist"
        suggestion = "Good listening session"

    else:
        category = "Irregular Playlist"
        suggestion = "Adjust song durations for better flow"

    print("Total Duration:", total, "seconds")
    print("Songs:", songs)
    print("Category:", category)
    print("Recommendation:", suggestion)