

# randomOrNull

Returns a random element from this array, or null if this array is empty.

```kotlin
inline fun <T> Array<out T>.randomOrNull(): T?(source)
```

```kotlin
fun main() {
    val empty = arrayOf<String>()
    println(empty.randomOrNull()) // null

    val colors = arrayOf("red", "green", "blue")
    println(colors.randomOrNull()) // random color from the array
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/random-or-null.html)

    