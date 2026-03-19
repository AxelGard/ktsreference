

# toFloatArray

Returns an array of Float containing all of the elements of this generic array.

```kotlin
fun Array<out Float>.toFloatArray(): FloatArray(source)
```

```kotlin
fun main() {
    val floatObjects: Array<Float> = arrayOf(1.2f, 3.4f, 5.6f)
    val primitiveArray: FloatArray = floatObjects.toFloatArray()
    println(primitiveArray.contentToString()) // prints [1.2, 3.4, 5.6]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-float-array.html)

    