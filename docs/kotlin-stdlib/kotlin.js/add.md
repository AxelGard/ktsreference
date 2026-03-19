

# add

Adds key-value pairs from other to this. Returns the original receiver.

```kotlin
fun Json.add(other: Json): Json(source)
```

```kotlin
import kotlin.js.Json

val base: Json = js("{x: 10}")
val other: Json = js("{y: 20, z: 30}")

base.add(other)

println(JSON.stringify(base))  // {"x":10,"y":20,"z":30}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/add.html)

    