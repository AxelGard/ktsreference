

# downTo

Returns a progression from this value down to and including the specified to value with the step -1.

```kotlin
infix fun Int.downTo(to: Byte): IntProgression(source)
```

```kotlin
val end: Byte = 3

for (i in 7 downTo end) {
    println(i)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/down-to.html)

    