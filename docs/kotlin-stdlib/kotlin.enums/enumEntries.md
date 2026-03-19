

# enumEntries

Returns EnumEntries list containing all enum entries for the given enum type T.

```kotlin
inline fun <T : Enum<T>> enumEntries(): EnumEntries<T>(source)
```

```kotlin
enum class Color { RED, GREEN, BLUE }

fun main() {
    val colors = enumEntries<Color>()          // Get all enum entries
    for (c in colors) {
        println(c)                            // Prints: RED, GREEN, BLUE
    }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/enum-entries.html)

    