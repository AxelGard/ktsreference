

# findAssociatedObject

If T is an @AssociatedObjectKey-annotated annotation class and this class is annotated with @T (S::class), returns object S.

```kotlin
actual inline fun <T : Annotation> KClass<*>.findAssociatedObject(): Any?(source)
```

```kotlin
import kotlin.reflect.AssociatedObjectKey
import kotlin.reflect.full.findAssociatedObject

@Target(AnnotationTarget.CLASS)
@AssociatedObjectKey
annotation class Service(val provider: KClass<*>)

object DatabaseProvider

@Service(DatabaseProvider::class)
class Repository

fun main() {
    val provider = Repository::class.findAssociatedObject<Service>()
    println(provider) // prints DatabaseProvider
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/find-associated-object.html)

    