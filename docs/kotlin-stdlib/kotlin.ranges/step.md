

# step

Returns a progression that goes over the same range with the given step.

```kotlin
infix fun IntProgression.step(step: Int): IntProgression(source)
```

```kotlin
fun main() {
    val progression = (1..10) step 2
    for (i in progression) {
        println(i)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/step.html)

    