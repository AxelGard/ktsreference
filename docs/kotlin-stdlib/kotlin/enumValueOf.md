

# enumValueOf

Returns an enum entry with specified name.

```kotlin
expect inline fun <T : Enum<T>> enumValueOf(name: String): T(source)
```

```kotlin
enum class Direction { NORTH, SOUTH, EAST, WEST }

fun main() {
    val dirName = "EAST"
    val direction = enumValueOf<Direction>(dirName)
    println(direction) // Output: EAST
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/enum-value-of.html)

    