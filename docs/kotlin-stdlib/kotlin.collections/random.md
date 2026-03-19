

# random

Returns a random element from this array.

```kotlin
inline fun <T> Array<out T>.random(): T(source)
```

```kotlin
fun main() {
    val colors = arrayOf("red", "green", "blue", "yellow")
    val randomColor = colors.random()
    println("Random color: $randomColor")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/random.html)

    