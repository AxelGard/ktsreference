

# toBooleanArray

Returns an array of Boolean containing all of the elements of this generic array.

```kotlin
fun Array<out Boolean>.toBooleanArray(): BooleanArray(source)
```

```kotlin
fun main() {
    val kotlinArray = arrayOf(true, false, true)
    val booleanArray: BooleanArray = kotlinArray.toBooleanArray()
    println(booleanArray.contentToString())  // prints: [true, false, true]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-boolean-array.html)

    