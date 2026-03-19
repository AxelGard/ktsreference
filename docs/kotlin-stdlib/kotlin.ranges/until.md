

# until

Returns a range from this value up to but excluding the specified to value.

```kotlin
infix fun Int.until(to: Byte): IntRange(source)
```

```kotlin
fun main() {
    val max: Byte = 5
    for (i in 0 until max) {
        println(i)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/until.html)

    