

# reversed

Returns a progression that goes over the same range in the opposite direction with the same step.

```kotlin
fun IntProgression.reversed(): IntProgression(source)
```

```kotlin
val range = 1..5                 // 1, 2, 3, 4, 5
val reversed = range.reversed()  // 5, 4, 3, 2, 1

for (i in reversed) {
    println(i)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/reversed.html)

    