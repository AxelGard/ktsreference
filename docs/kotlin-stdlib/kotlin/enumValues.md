

# enumValues

Returns an array containing enum T entries.

```kotlin
expect inline fun <T : Enum<T>> enumValues(): Array<T>(source)
```

```kotlin
enum class Color {
    RED, GREEN, BLUE
}

fun main() {
    val colors = enumValues<Color>()
    colors.forEach { println(it) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/enum-values.html)

    